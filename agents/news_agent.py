import os
import google.generativeai as genai

# Mengambil kunci dari environment variable yang diset GitHub Actions
api_key = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro')

def get_exos_intelligence():
    print("--- EXOS+ GLOBAL INTELLIGENCE HUB ---")
    
    if not api_key:
        print("Error: GOOGLE_API_KEY tidak ditemukan.")
        return

    prompt = "Berikan analisis singkat emisi karbon dan kebijakan fiskal global hari ini."
    
    try:
        response = model.generate_content(prompt)
        print("\nSTRATEGIC REPORT:")
        print(response.text)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_exos_intelligence()
