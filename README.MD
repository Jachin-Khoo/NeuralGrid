# AI Hydroponic Doctor

## Project Description

The **AI Hydroponic Doctor** is an automated multi-agent system designed to assist hydroponic farmers and hobbyists in maintaining plant health. Diagnosing nutrient deficiencies and calculating precise chemical corrections is often complex and error-prone.

This solution leverages **Google Gemini 2.5 Flash** to create a three-stage pipeline:

1. **Vision Agent:** Analyzes plant images to identify visual symptoms (chlorosis, necrosis, etc.).
2. **Diagnostician Agent:** Cross-references observed symptoms with a standard plant pathology guide (`plant_symptom.pdf`) to determine the specific nutrient deficiency.
3. **Chemist Agent:** Consults a dosage guide (`dosage_guide.pdf`) to calculate the exact mass of fertilizer salts required to correct the issue based on the user's water reservoir volume.

## Setup Instructions

### Prerequisites

* Python 3.9 or higher
* A Google Cloud Project with the Gemini API enabled
* A Gemini API Key

### 1. Clone or Download the Repository

Ensure all script files (`main.py`, `config.py`, `agent_*.py`) are in the same directory.

### 2. Install Dependencies

Install the required Python packages using pip:

```bash
pip install google-genai python-dotenv

```

### 3. Configure Environment Variables

Create a file named `.env` in the root directory of the project. Add your Gemini API key:

```env
GEMINI_API_KEY=your_actual_api_key_here

```

### 4. Prepare Reference Materials

The system requires two specific PDF knowledge bases to function. Place the following files in the root directory:

* `plant_symptom.pdf`: A document mapping visual symptoms to nutrient deficiencies.
* `dosage_guide.pdf`: A document listing fertilizer salts, target concentrations (ppm), and chemical properties.

## Usage Guide

### 1. Run the Application

Execute the main script from your terminal:

```bash
python main.py

```

### 2. Follow the Prompts

The system will ask for two inputs:

1. **Image Filename:** Enter the path to the photo of your sick plant (e.g., `tomato_leaf.jpg`). *Note: This image must exist in the project folder.*
2. **Water Volume:** Enter the size of your hydroponic reservoir in Liters.

### 3. View Results

The AI will output a sequential analysis:

* **[OBSERVATION]:** Detailed visual description of the symptoms.
* **[DIAGNOSIS]:** The specific element identified as deficient (e.g., "Magnesium").
* **[PRESCRIPTION]:** A calculation of exactly how many grams of a specific chemical to add to your reservoir.

### Example Output

```text
=== AI HYDROPONIC DOCTOR ===
> Please enter the filename of your plant image: basil_yellow.jpg
> Enter water volume (Liters): 50

[OBSERVATION]:
The plant exhibits interveinal chlorosis on older leaves, with veins remaining green. No necrosis is visible...

[DIAGNOSIS]: Magnesium

[PRESCRIPTION]:
To correct the Magnesium deficiency, add 12.3 grams of Magnesium Sulfate (Epsom Salt).
Calculation: (Target 25mg/L * 50L) / 1000 = 1.25g (Example)

```

## Deployment Instructions

To deploy this solution to a cloud environment (e.g., Google Cloud Run or a VM):

1. **Containerization:**
Create a `Dockerfile` to package the scripts and dependencies:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install google-genai python-dotenv
CMD ["python", "main.py"]

```


2. **Environment Secrets:**
Do not commit the `.env` file. Inject the `GEMINI_API_KEY` as an environment variable in your cloud provider's secret manager.
3. **File Persistence:**
In a production environment, you may want to modify `agent_uploader.py` to accept file streams from a web frontend rather than local file paths, and store the reference PDFs in Google Cloud Storage or upload them once and cache the file URIs.

## Contributors

* Yeo Wei Ting
* Jachin Khoo Yangxun
* Chloe Cheo
* Soon Zi Ni Darlene
* Tan Le Jie
* Suh Sumin

## Additional Notes

* **Model Version:** This project uses `gemini-2.5-flash`. Ensure your API key has access to this specific model version.
* **PDF Formatting:** The accuracy of the Diagnosis and Chemist agents depends heavily on the clarity of the text in `plant_symptom.pdf` and `dosage_guide.pdf`. Text-based PDFs work better than scanned images.
* **Disclaimer:** This tool provides AI-generated advice. Always verify chemical dosages manually before applying them to living plants, as AI can occasionally make calculation errors or hallucinations.
