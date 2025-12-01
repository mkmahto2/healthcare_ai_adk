drug_database = {
    "paracetamol": {
        "uses": "Fever, mild pain relief",
        "dosage": "500mg every 6-8 hours",
        "warning": "Avoid overdose. Safe max 3g/day."
    },
    "azithromycin": {
        "uses": "Bacterial infections",
        "dosage": "500mg once daily",
        "warning": "Use only with prescription."
    }
}

def get_drug_info(name: str):
    name = name.lower()
    if name in drug_database:
        info = drug_database[name]
        return f"""
Drug: {name.capitalize()}
Uses: {info['uses']}
Dosage: {info['dosage']}
Warning: {info['warning']}
"""
    return "Drug not found."
