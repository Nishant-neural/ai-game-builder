from utils import call_ollama

def generate_phaser_code(gdd: dict):
    system_prompt = f"""
You are a Phaser 3 expert.

Generate a COMPLETE working Phaser game in ONE HTML file.

Rules:
- Use Phaser CDN
- Include player movement
- Include at least one mechanic from: {gdd["mechanics"]}
- No explanations
- Return ONLY HTML
"""

    return call_ollama(system_prompt, str(gdd))