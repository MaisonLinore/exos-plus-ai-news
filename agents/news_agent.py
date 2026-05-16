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
            model="gemini-1.5-flash",  # <-- PERUBAHAN DI SINI
            contents="Berikan 3 berita AI terbaru dalam bahasa Indonesia. Format: - Berita 1, - Berita 2, - Berita 3",
        )
        print("\n📰 HASIL BERITA AI TERKINI:\n")
        print(response.text)
        print("\n✅ Selesai.")
    except Exception as e:
        print(f"❌ Gagal: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
