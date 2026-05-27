from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import simulation
from app.routers import websocket

app = FastAPI(
    title="Anti bio",
    description="Anti bio",
    version="0.0.1",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*","null"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(simulation.router)
app.include_router(websocket.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
