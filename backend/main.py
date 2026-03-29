from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pipeline.gdd_agent import generate_gdd
from pipeline.code_agent import generate_phaser_code

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate-game")
def generate_game(data: dict):
    prompt = data["prompt"]

    # Step 1: GDD
    gdd = generate_gdd(prompt)

    # Step 2: Code
    code = generate_phaser_code(gdd)

    return {
        "gdd": gdd,
        "code": code
    }
