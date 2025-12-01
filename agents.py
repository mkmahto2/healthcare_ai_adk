

from google import genai
from config import GEMINI_API_KEY, MODEL_NAME

from tools.medical_search import medical_search
from tools.drug_info import get_drug_info
from tools.symptom_checker import symptom_checker
from tools.safety_layer import safety_filter

client = genai.Client(api_key=GEMINI_API_KEY)

def healthcare_agent(prompt: str):
    # Safety Check
    safety_issue = safety_filter(prompt)
    if safety_issue:
        return safety_issue

    # If asking about drug
    if "medicine" in prompt.lower() or "drug" in prompt.lower():
        words = prompt.split()
        for w in words:
            result = get_drug_info(w)
            if "Drug:" in result:
                return result

    # Symptom checker
    if "symptom" in prompt.lower() or "feel" in prompt.lower():
        return symptom_checker(prompt.lower().split())

    # Ask Gemini
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=f"""
You are a safe medical healthcare AI agent. 
Provide helpful but non-diagnostic advice.

User Query: {prompt}
"""
    )
    return response.text
