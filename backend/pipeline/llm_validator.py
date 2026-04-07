from utility.utils import call_ollama
import json
def filter_errors(errors):
    allowed = [
        "physics",
        "sprite",
        "scene",
        "preload",
        "score",
        "collision"
    ]

    return [
        e for e in errors
        if any(k in e.lower() for k in allowed)
    ]

def llm_validate(code: str):
    system_prompt = """
You are a Phaser 3 game engine expert.

Analyze the code and find issues.

STRICT RULES:
- Only report REAL errors
- Do NOT invent issues
- Focus on runtime correctness
- return only a JSON array of errors
- DO NOT add  explanation.

Check for:
- invalid APIs
- wrong physics usage
- missing logic
- broken game behavior

Return ONLY a JSON array of errors:
["error1", "error2"]
"""

    user_prompt = f"""
Code:
{code}
"""

    output = call_ollama(system_prompt, user_prompt)
   
    try:
        output = json.loads(output)
        return filter_errors(output)
    except:
        return ["LLM validation failed"]