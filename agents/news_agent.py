import os
import sys
from google import genai

def main():
    print("--- EXOS+ GLOBAL INTELLIGENCE HUB ---")
    
    # Ambil API key dari environment variable
    api_key = os.getenv("AIzaSyDMnRYXwrgQ7auOPT1__Q7Rbiw9NNReZ3E")
    if not api_key:
        print("❌ ERROR: GOOGLE_API_KEY tidak ditemukan di environment.")
        print("Pastikan secret sudah diatur dengan benar di GitHub Actions.")
        sys.exit(1)
    
    print("✅ API key ditemukan. Menghubungi Gemini API...")
    
    try:
        # Inisialisasi client
        client = genai.Client(api_key=api_key)
        
        # Prompt sederhana untuk berita AI
        prompt = "Berikan 3 berita terbaru tentang Artificial Intelligence (AI) dalam bahasa Indonesia. Format: - Berita 1, - Berita 2, - Berita 3"
        
        # Panggil model Gemini (gratis)
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",  # atau "gemini-1.5-flash"
            contents=prompt,
        )
        
        print("\n📰 HASIL BERITA AI TERKINI:\n")
        print(response.text)
        print("\n✅ Eksekusi selesai.")
        
    except Exception as e:
        print(f"❌ Gagal memanggil Gemini API: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
