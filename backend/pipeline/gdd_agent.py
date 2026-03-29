import json
from utils import call_ollama

def generate_gdd(prompt: str):
    system_prompt = """
You are a game designer.

Return ONLY valid JSON:
{
  "genre": "",
  "core_loop": "",
  "player_goal": "",
  "mechanics": []
}
"""

    output = call_ollama(system_prompt, prompt)

    try:
        return json.loads(output)
    except:
        # fallback: extract JSON
        start = output.find("{")
        end = output.rfind("}") + 1
        return json.loads(output[start:end])