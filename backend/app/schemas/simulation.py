from pydantic import BaseModel,Field

class SimulationRequest(BaseModel):
    antibiotic_name:str = Field(min_length=1, max_length=100)
    molecule_chembl_id: str = Field(min_length=1)
    concentration: float = Field(gt=0, description="농도는 (ug/mL),0 초과")
    temperature: float = Field(ge=0,le=42,description="온도 (C),4~42")
    environment_ph: float = Field(ge=0,le=9.0,description="pH 범위 4~9")
    ecoil_strain: str = Field(min_length=1, max_length=50)

class SimulationResponse(BaseModel):
    antibiotic_name:str
    concentration: float
    survival_rate: float
    resistance_analysis: str
    mic_value: float
