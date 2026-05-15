import os
import sys
from google import genai

def main():
    print("--- EXOS+ GLOBAL INTELLIGENCE HUB ---")
    api_key = os.getenv("AIzaSyDMnRYXwrgQ7auOPT1__Q7Rbiw9NNReZ3E")
    if not api_key:
        print("ERROR: GOOGLE_API_KEY tidak ditemukan.")
        sys.exit(1)
    print("API key ditemukan, memproses...")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash-exp",
        contents="Berita AI terbaru dalam 3 poin.",
    )
    print(response.text)

if __name__ == "__main__":
    main()
