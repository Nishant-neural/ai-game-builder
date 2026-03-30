from utility.utils import call_ollama
from rag.retreiver import retrieve_context

def correct_code(code: str, errors: list , prev_errors: list):
    context = retrieve_context(" ".join(errors))

    system_prompt = f"""
You are a Phaser 3 expert debugger.

Fix the provided game code STRICTLY.
Do NOT introduce new classes, systems, or features.
Only fix existing code.

STRICT RULES:
- Return ONLY valid HTML
- Do NOT include markdown
- ONLY fix the errors listed
- DO NOT rewrite entire code
- DO NOT add new features
- DO NOT change working parts

CONTEXT : {context}

Errors to fix:
{errors}

If you introduce new errors, you FAILED.
Ensure Phaser APIs are valid.
"""
    if errors == prev_errors:
        system_prompt += """
You FAILED to fix errors previously.
Now STRICTLY fix ONLY listed issues.
Do NOT rewrite code.
"""

    user_prompt = f"""
 Broken Code:
{code}

Fix only the problematic parts.
Return fixed version.
"""

    return call_ollama(system_prompt, user_prompt)