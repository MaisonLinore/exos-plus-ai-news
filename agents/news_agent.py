#!/usr/bin/env python3
# Exos+ Global Intelligence Hub - News Agent
# Menggunakan library google.genai yang terbaru

import os
import sys
from google import genai
from google.genai import types

def main():
    print("--- EXOS+ GLOBAL INTELLIGENCE HUB ---")
    
    # Ambil API key dari environment variable
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("❌ ERROR: GOOGLE_API_KEY tidak ditemukan.")
        print("Pastikan environment variable GOOGLE_API_KEY sudah diset.")
        print("Di GitHub Actions, pastikan secret 'GOOGLE_API_KEY' sudah diisi.")
        sys.exit(1)
    
    print("✅ API key ditemukan, mencoba menghubungi Gemini...")
    
    try:
        # Inisialisasi client dengan API key
        client = genai.Client(api_key=api_key)
        
        # Contoh prompt: berita AI terkini
        prompt = """
        Berikan ringkasan berita terbaru tentang Artificial Intelligence (AI) 
        dalam 3 poin singkat. Format:
        - [Judul berita] (sumber fiktif)
        """
        
        # Panggil model Gemini 2.0 Flash (cepat & gratis)
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",  # atau "gemini-1.5-flash" untuk stabil
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.7,
                max_output_tokens=300,
            )
        )
        
        print("\n📰 **HASIL BERITA AI TERKINI:**\n")
        print(response.text)
        print("\n✅ Eksekusi selesai.")
        
    except Exception as e:
        print(f"❌ Terjadi kesalahan saat memanggil Gemini API: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
