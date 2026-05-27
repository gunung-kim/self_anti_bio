from google import genai

from app.core.config import settings

client = genai.Client(api_key=settings.GEMINI_KEY)

async def analyze_resistance(mic_value:float,concentration:float,antibiotic_name:str)->str:
    prompt = (
        f"항생제 : {antibiotic_name}\n"
        f"MIC : {mic_value}ug/mL\n"
        f"투여 농도 : {concentration}ug/mL%\n"
        "위 정보를 바탕으로 대장균의 내성 가능성과 대안 약물을 JSON 형태로 반환해줘. \n"
        "반드기 JSON만 반환하고 마크다운 코드블록 없이 순수한 JSON만 한글로 출력해.\n"
        '형식 : {"resistance_level":"high/medium/low","reason":"...","alternatives":[...]}'
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text