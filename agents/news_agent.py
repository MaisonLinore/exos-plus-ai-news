import os
import sys
from google import genai

def main():
    print("--- EXOS+ GLOBAL INTELLIGENCE HUB ---")
    
    # Ambil API key dari environment variable (dikirim dari GitHub Actions)
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("❌ ERROR: GOOGLE_API_KEY tidak ditemukan di environment.")
        print("Pastikan secret 'GOOGLE_API_KEY' sudah diisi di GitHub repository.")
        sys.exit(1)
    
    print("✅ API key ditemukan. Menghubungi Gemini API...")
    
    try:
        client = genai.Client(api_key=api_key)
        prompt = "Berikan 3 berita terbaru tentang AI dalam bahasa Indonesia. Format: - Berita 1, - Berita 2, - Berita 3"
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=prompt,
        )
        print("\n📰 HASIL BERITA AI TERKINI:\n")
        print(response.text)
        print("\n✅ Selesai.")
    except Exception as e:
        print(f"❌ Gagal: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
