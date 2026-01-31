import streamlit as st
import google.generativeai as genai
import os

# 1. Configuration
st.set_page_config(page_title="Medi-Path AI", page_icon="🏥")
genai.configure(api_key="YOUR_API_KEY_HERE") # Use environment variables later
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. UI Elements
st.title("🏥 Medi-Path AI")
st.subheader("Post-Discharge Patient Assistant")

query = st.text_area("How are you feeling today?", placeholder="e.g., I have a slight fever but my incision looks clean.")

if st.button("Analyze Symptoms"):
    if query:
        # 3. Dual-Path Logic (Safety Filter)
        emergency_keywords = ["chest pain", "shortness of breath", "heavy bleeding", "unconscious"]
        
        if any(word in query.lower() for word in emergency_keywords):
            st.error("🚨 EMERGENCY DETECTED: Please contact emergency services immediately.")
        else:
            # 4. Generative AI Path
            with st.spinner("Analyzing recovery data..."):
                prompt = f"Patient Query: {query}. Provide supportive recovery advice based on standard post-operative care."
                response = model.generate_content(prompt)
                st.info(response.text)
    else:
        st.warning("Please enter your symptoms.")