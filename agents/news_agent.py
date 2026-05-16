import os
import sys
from google import genai

def main():
    print("--- EXOS+ GLOBAL INTELLIGENCE HUB ---")
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("❌ ERROR: GOOGLE_API_KEY tidak ditemukan.")
        sys.exit(1)
    
    print("✅ API key ditemukan. Menghubungi Gemini API...")
    
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",  # <-- PERUBAHAN DI SINI
            contents="Give 3 update AI news in English. Format: - News 1, - News 2, - Newss 3",
        )
        print("\n📰 RESULTS UPDATE AI NEWS.\n")
        print(response.text)
        print("\n✅ Done.")
    except Exception as e:
        print(f"❌ Failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
