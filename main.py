# main.py
import os
from dotenv import load_dotenv

load_dotenv()  

from agent_uploader import upload_file_to_gemini
from agent_vision import agent_vision_analyze
from agent_diagnostician import agent_diagnose_deficiency
from agent_chemist import agent_calculate_dosage

def main():
    print("=== AI HYDROPONIC DOCTOR ===")

    symptoms_file = "plant_symptom.pdf"
    dosage_file = "dosage_guide.pdf"

    if not os.path.exists(symptoms_file) or not os.path.exists(dosage_file):
        print(
            f"ERROR: Missing files.\nPlease ensure '{symptoms_file}' and '{dosage_file}' are in this folder."
        )
        return

    while True:
        image_input = input(
            "\n> Please enter the filename of your plant image (e.g., photo.jpg): "
        ).strip()
        image_input = image_input.replace('"', "").replace("'", "")

        if os.path.exists(image_input):
            break
        else:
            print("  File not found. Please try again.")

    while True:
        try:
            vol_input = input("> Enter water volume (Liters): ")
            volume = float(vol_input)
            break
        except ValueError:
            print("  Please enter a valid number.")

    print("\n--- Starting Diagnosis Pipeline ---\n")

    symptoms_pdf_ref = upload_file_to_gemini(
        symptoms_file, mime_type="application/pdf"
    )
    dosage_pdf_ref = upload_file_to_gemini(dosage_file, mime_type="application/pdf")

    if not symptoms_pdf_ref or not dosage_pdf_ref:
        print("ERROR: Failed to upload reference PDFs. Exiting.")
        return

    symptoms_desc = agent_vision_analyze(image_input)
    if not symptoms_desc:
        print("ERROR: Failed to analyze plant image.")
        return
    print(f"\n[OBSERVATION]:\n{symptoms_desc}")

    deficiency = agent_diagnose_deficiency(symptoms_desc, symptoms_pdf_ref)
    print(f"\n[DIAGNOSIS]: {deficiency}")

    if not deficiency or len(deficiency.split()) > 3:
        print(
            "WARNING: Diagnosis output looks unusual. Please verify before applying nutrients."
        )

    final_prescription = agent_calculate_dosage(deficiency, volume, dosage_pdf_ref)
    print(f"\n[PRESCRIPTION]:\n{final_prescription}")

if __name__ == "__main__":
    main()
