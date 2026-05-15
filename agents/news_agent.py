import os
import google.generativeai as genai

# Konfigurasi AI
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def get_exos_intelligence():
    print("--- EXOS+ GLOBAL INTELLIGENCE HUB ---")
    
    # Prompt khusus untuk News Agent
    prompt = """
    Analyze today's global news with focus on:
    1. Carbon Emissions & ESG Standards.
    2. National Fiscal Policy Stimulus.
    3. Macroeconomic shifts.
    Output must be Exclusive, Smart, and Elegant in Indonesian.
    """
    
    try:
        response = model.generate_content(prompt)
        print("\nSTRATEGIC REPORT:")
        print(response.text)
    except Exception as e:
        print(f"Connection Error: {e}")

if __name__ == "__main__":
    get_exos_intelligence()
