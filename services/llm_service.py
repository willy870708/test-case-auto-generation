# services/llm_service.py
import google.generativeai as genai
from core.config import settings
import json

genai.configure(api_key=settings.GEMINI_API_KEY)

def _build_prompt(code: str, language: str, framework: str) -> str:
    return f"""
You are an expert test engineer. Your task is to generate both test case documentation and test code for the given source code.
Language: {language}
Testing Framework: {framework}

Source Code:
Provide the output in a single JSON object with two keys: "test_cases_doc" (a string with markdown list of test scenarios) and "test_cases_code" (a string containing the complete, runnable test code).
"""

async def generate_test_cases_from_llm(code: str, language: str, framework: str) -> dict:
    prompt = _build_prompt(code, language, framework)
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        generation_config = genai.types.GenerationConfig(response_mime_type="application/json")
        
        response = await model.generate_content_async(
            prompt,
            generation_config=generation_config
        )
        
        result = json.loads(response.text)
        
        if "test_cases_doc" in result and "test_cases_code" in result:
            return result
        else:
            raise ValueError("Gemini response is missing required keys.")
            
    except Exception as e:
        print(f"Gemini service error: {e}")
        raise