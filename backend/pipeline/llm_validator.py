from utility.utils import call_ollama

def llm_validate(code: str):
    system_prompt = """
You are a Phaser game engine expert.

Analyze the code and find issues.

STRICT RULES:
- Only report REAL errors
- Do NOT invent issues
- Focus on runtime correctness
- return a JSON list of errors

Check for:
- invalid APIs
- wrong physics usage
- missing logic
- broken game behavior

Return ONLY a JSON list of errors:
["error1", "error2"]
"""

    user_prompt = f"""
Code:
{code}
"""

    output = call_ollama(system_prompt, user_prompt)

    try:
        return eval(output) 
    except:
        return ["LLM validation failed"]