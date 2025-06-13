import google.generativeai as genai
import os
from dotenv import load_dotenv
import asyncio

# --- This is our sole objective: find available models ---

async def main():
    # Load environment variables from the .env file
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("Error: GEMINI_API_KEY not found. Please check your .env file.")
        return

    # Configure the API key
    try:
        genai.configure(api_key=api_key)
        print("API key configured successfully. Querying available models...")
    except Exception as e:
        print(f"Failed to configure API key: {e}")
        return

    # List all available models
    print("\n--- List of Available Models (supporting generateContent) ---\n")
    try:
        model_found = False
        for m in genai.list_models():
            # We are only interested in models that can be used to generate content
            if 'generateContent' in m.supported_generation_methods:
                print(f"   - {m.name}")
                model_found = True

        if not model_found:
            print("No models supporting 'generateContent' found.")

    except Exception as e:
        print(f"\nAn error occurred while querying models: {e}")
        print("\n--- Debugging Suggestions ---")
        print("1. Please ensure 'Generative Language API' is enabled for your Google Cloud project.")
        print("   Enable it here: https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com")
        print("2. Please ensure your project is linked to a valid billing account. Access to some models requires billing to be enabled.")
        print("3. Please ensure your Google account or project does not have any regional restrictions or error states.")

if __name__ == "__main__":
    asyncio.run(main())