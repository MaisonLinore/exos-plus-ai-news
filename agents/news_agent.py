import os
from google import genai

# Menggunakan pustaka google-genai terbaru
def get_exos_intelligence():
    print("--- EXOS+ GLOBAL INTELLIGENCE HUB ---")
    
    # Mengambil kunci dari GitHub Secrets
    api_key = os.environ.get("GOOGLE_API_KEY")
    
    if not api_key:
        print("Error: GOOGLE_API_KEY tidak ditemukan di environment.")
        return

    client = genai.Client(api_key=api_key)
    
    prompt = """
    Analyze today's global news with focus on:
    1. Carbon Emissions & ESG Standards.
    2. National Fiscal Policy Stimulus.
    3. Macroeconomic shifts.
    Output must be Exclusive, Smart, and Elegant in Indonesian.
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=prompt
        )
        print("\nSTRATEGIC REPORT:")
        print(response.text)
    except Exception as e:
        print(f"Strategic Error: {e}")

if __name__ == "__main__":
    get_exos_intelligence()
