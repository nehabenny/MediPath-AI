import PyPDF2
from google import genai
import os

def process_medical_pdf(file_path):
    # 1. Extract text from PDF
    with open(file_path, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
            
    # 2. Ask Gemini to analyze it
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    response = client.models.generate_content(
        model="gemini-1.5-flash", 
        contents=f"Extract key red flags from this discharge summary: {text}"
    )
    return response.text