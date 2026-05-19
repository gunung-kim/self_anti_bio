from fastapi import HTTPException
from starlette import status

from app.schemas.simulation import SimulationRequest, SimulationResponse
from app.services.chembl import get_mic_data
from app.services.gmini import analyze_resistance
from app.services.hill import hill_equation


async def get_simulation(request:SimulationRequest)->SimulationResponse:
    # 1.ChEMBL에서 MIC 데이터 가져오기
    mic_data = await get_mic_data(request.molecule_chembl_id)
    activities = mic_data.get('activities',[])

    # 2, MIC 평군값 계산
    mic_value = [
        float(a["standard_value"])
        for a in activities
        if a.get("standard_value")
    ]
    if not mic_value:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="해당 약물에 대한 mic 값이 없습니다"
        )
    mic_avg = sum(mic_value)/len(mic_value)

    # 3. Hill 방정식으로 생존률 계산
    survival_rate = hill_equation(
        concentration=request.concentration,
        mic=mic_avg
    )

    # 4.Gemini로 내성 분석
    resistance_analysis = await analyze_resistance(
        mic_value=mic_avg,
        concentration=request.concentration,
        antibiotic_name=request.antibiotic_name,
    )

    return SimulationResponse(
        antibiotic_name=request.antibiotic_name,
        concentration=request.concentration,
        survival_rate=survival_rate,
        resistance_analysis=resistance_analysis,
        mic_value=mic_avg
    )