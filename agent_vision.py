# agent_vision.py
from config import client, MODEL_NAME
from agent_uploader import upload_file_to_gemini

def agent_vision_analyze(image_path):
    print("\n--- Agent 1: Analyzing Visual Symptoms ---")

    plant_image = upload_file_to_gemini(image_path, mime_type="image/jpeg")
    if not plant_image:
        return None

    prompt = """
You are an expert plant pathologist. Analyze this image.
Describe the plant's condition in detail, focusing ONLY on diagnostic symptoms.
Look for:
1. Leaf coloration (chlorosis, yellowing veins, purple undersides).
2. Necrosis (brown spots, burnt tips).
3. Structural issues (curling, stunting, wilting).

Output a concise but detailed description of the symptoms.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[prompt, plant_image],
    )
    return response.text
