from fastapi import APIRouter

from app.schemas.simulation import SimulationResponse, SimulationRequest
from app.services.simulation import get_simulation
router = APIRouter(prefix="/simulation",tags=["simulation"])

@router.post("/run",response_model=SimulationResponse)
async def run_simulation(request: SimulationRequest) -> SimulationResponse:
    return await get_simulation(request)

