import google.generativeai as genai

from app.core.config import settings

genai.configure(api_key=settings.GEMINI_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

async def analyze_resistance(mic_value:float,concentration:float,antibiotic_name:str)->str:
    prompt = (
        f"항생제 : {antibiotic_name}\n"
        f"MIC : {mic_value}ug/mL\n"
        f"투여 농도 : {concentration}%\n"
        "위 정보를 바탕으로 대장균의 내성 가능성과 대안 약물을 JSON 형태로 반환해줘. \n"
        '형식 : {"resistance_level":"high/medium/low","reason":"...","alternatives":[...]}'
    )
    response = model.generate_content(prompt)
    return response.text