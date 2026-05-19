from fastapi import FastAPI

from app.routers import simulation

app = FastAPI(
    title="Anti bio",
    description="Anti bio",
    version="0.0.1",
)

app.include_router(simulation.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
