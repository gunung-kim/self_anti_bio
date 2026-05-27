from app.services.chembl import get_mic_data
from app.services.hill import hill_equation
from fastapi import APIRouter
from starlette.websockets import WebSocket

router = APIRouter()


@router.websocket("/ws/simulation")
async def simulation_websocket(websocket: WebSocket):
    await websocket.accept()
    data = await websocket.receive_json()

    molecule_chembl_id = data.get("molecule_chembl_id")
    concentration = float(data.get("concentration"))
    days = int(data.get("days", 30))
    resistance_rate = float(data.get("resistance_rate", 0.1))

    try:
        mic_data = await get_mic_data(molecule_chembl_id)
    except Exception as e:
        await websocket.send_json({"error": str(e)})
        await websocket.close()
        return
    activities = [
        a
        for a in mic_data.get("activities", [])
        if "coli" in (a.get("target_organism") or "").lower()
    ]
    mic_values = [
        float(a["standard_value"]) for a in activities if a.get("standard_value")
    ]
    mic_values = [v for v in mic_values if v < 1000]

    if not mic_values:
        await websocket.send_json({"error": "MIC 데이터 없음"})
        await websocket.close()
        return

    mic_base = sum(mic_values) / len(mic_values)

    for day in range(1, days + 1):
        mic = mic_base * ((1 + resistance_rate) ** day)
        survival = hill_equation(concentration=concentration, mic=mic)
        await websocket.send_json(
            {"day": day, "mic": round(mic, 4), "survival_rate": round(survival, 4)}
        )

    await websocket.close()
