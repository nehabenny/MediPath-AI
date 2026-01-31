import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. Setup
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API Key missing! Check your .env file.")
else:
    genai.configure(api_key=api_key)
    # Changed to a valid model name
    model = genai.GenerativeModel('gemini-2.5-flash')

    # 2. UI
    st.title("🏥 Medi-Path AI")
    st.subheader("Post-Discharge Patient Assistant")

    query = st.text_area("How are you feeling today?", placeholder="e.g., I have a slight fever...")

    if st.button("Analyze Symptoms"):
        if query:
            emergency_keywords = ["chest pain", "shortness of breath", "heavy bleeding", "unconscious"]
            
            if any(word in query.lower() for word in emergency_keywords):
                st.error("🚨 EMERGENCY DETECTED: Please contact emergency services immediately.")
            else:
                with st.spinner("Analyzing..."):
                    try:
                        prompt = f"Patient Query: {query}. Provide supportive recovery advice based on standard post-operative care."
                        response = model.generate_content(prompt)
                        st.info(response.text)
                    except Exception as e:
                        st.error(f"An error occurred: {e}")