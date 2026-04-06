from utility.utils import call_ollama
from rag.retreiver import retrieve_context
from memory.memory_store import load_memory

def correct_code(code: str, errors: list , prev_errors: list):
    memory = load_memory()
    context = retrieve_context(" ".join(errors))

    system_prompt = f"""
You are a Phaser 3 expert debugger.

Fix the provided game code STRICTLY.
Do NOT introduce new classes, systems, or features.
Only fix existing code.

STRICT RULES:
- Output only the corrected HTML, no explanation
- Do NOT include markdown
- ONLY fix the errors listed
- DO NOT rewrite entire code
- DO NOT add new features
- DO NOT change working parts
- Replace invalid methods with their correct Phaser 3 equivalents

DO NOT:
- remove physics system
- change scene structure
- introduce new classes
- modify config unless required

CONTEXT : {context}

Past mistakes:
{memory["errors"]}

Errors to fix:
{chr(10).join(f"- {e}" for e in errors)}

If you rewrite large sections , you FAILED.

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