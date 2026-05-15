import os
from google import genai
client = genai.Client(api_key= "AIzaSyDMnRYXwrgQ7auOPT1__Q7Rbiw9NNReZ3E")  # atau dari env
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Hello"
)
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
