# agent_diagnostician.py
from config import client, MODEL_NAME

def agent_diagnose_deficiency(symptoms_text, symptoms_pdf):
    print("\n--- Agent 2: Diagnosing Deficiency ---")

    prompt = f"""
You are an expert hydroponic diagnostician.

Based on the following observed symptoms:
\"\"\"{symptoms_text}\"\"\"

Consult the attached 'plant_symptom.pdf' guide. Match the symptoms to the most likely nutrient deficiency.

Output ONLY the name of the chemical element causing the issue (e.g., "Nitrogen", "Calcium", "Iron").
Do not add sentences, just the element name.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[prompt, symptoms_pdf],
    )
    return (response.text or "").strip()
