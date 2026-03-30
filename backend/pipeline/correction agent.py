from utils import call_ollama

def correct_code(code: str, errors: list):
    system_prompt = f"""
You are a Phaser 3 expert debugger.

Fix the provided game code.

STRICT RULES:
- Return ONLY valid HTML
- Do NOT include markdown
- Fix ALL errors listed
- Keep code simple and working

Errors to fix:
{errors}
"""

    user_prompt = f"""
Here is the broken code:
{code}

Return fixed version.
"""

    return call_ollama(system_prompt, user_prompt)