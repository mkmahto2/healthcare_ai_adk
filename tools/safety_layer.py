def safety_filter(user_input):
    unsafe_keywords = ["suicide", "self harm", "poison", "kill", "overdose"]

    for word in unsafe_keywords:
        if word in user_input.lower():
            return "⚠️ Safety Alert: I cannot assist with harmful or dangerous activities. Please contact a medical professional or emergency help."

    return None
