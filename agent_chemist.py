# agent_chemist.py
from config import client, MODEL_NAME

def agent_calculate_dosage(deficiency, water_volume, dosage_pdf):
    print("\n--- Agent 3: Calculating Chemical Dosage ---")

    prompt = f"""
You are a hydroponic chemist.

1. The diagnosed deficiency is: {deficiency}
2. The user's water reservoir volume is: {water_volume} Liters.

Using the attached 'dosage_guide.pdf':
- Identify the recommended fertilizer salt or chemical for correcting {deficiency}.
- Find the target concentration in mg/L (ppm).
- Calculate the exact mass in grams needed using the formula:
  Mass (g) = (Target mg/L * Volume Liters) / 1000

Output the result clearly:
"To correct the {deficiency} deficiency, add [X] grams of [Chemical Name]."
Show your calculation briefly.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[prompt, dosage_pdf],
    )
    return response.text
