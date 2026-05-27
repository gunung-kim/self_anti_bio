from app.schemas.simulation import SimulationRequest, SimulationResponse
from app.services.simulation import get_simulation
from fastapi import APIRouter

router = APIRouter(prefix="/simulation", tags=["simulation"])


@router.post("/run", response_model=SimulationResponse)
async def run_simulation(request: SimulationRequest) -> SimulationResponse:
    return await get_simulation(request)
