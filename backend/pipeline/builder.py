from pipeline.gdd_agent import generate_gdd
from pipeline.code_agent import generate_phaser_code

def run_pipeline(prompt: str):
    result = {
        "steps": []
    }

   
    gdd = generate_gdd(prompt)
    result["steps"].append({"stage": "gdd", "output": gdd})

    
    code = generate_phaser_code(gdd)
    result["steps"].append({"stage": "code", "output": code})

    return {
        "gdd": gdd,
        "code": code,
        "debug": result
    }