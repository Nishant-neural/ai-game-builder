from fastapi import FastAPI
from pipeline.builder import run_pipeline
from schemas import GameRequest

app = FastAPI()

@app.post("/generate-game")
def generate_game(request: GameRequest):
    print("Incoming prompt:", request.prompt)
    result = run_pipeline(request.prompt)
    return result