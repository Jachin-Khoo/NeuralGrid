# config.py
import os
from google import genai
from google.genai import types  

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("Please set GEMINI_API_KEY in your environment before running this script.")

client = genai.Client(api_key=API_KEY)
MODEL_NAME = "gemini-2.5-flash"
Types = types 
