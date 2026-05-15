import os
import google.generativeai as genai

# Setup Aeterna EM+
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def main():
    print("Exos+ Agentic AI News: Initiating Global ESG Analysis...")
    prompt = "Buat ringkasan eksklusif berita emisi karbon dan kebijakan fiskal global hari ini."
    try:
        response = model.generate_content(prompt)
        print(f"REPORT: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
