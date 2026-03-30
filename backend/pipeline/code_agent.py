from utility.utils import call_ollama
from rag.retreiver import retrieve_context

def generate_phaser_code(gdd: dict):
    context = retrieve_context(str(gdd))

    system_prompt = f"""
You are a Phaser 3 expert.

Generate a COMPLETE working Phaser game in ONE HTML file.

Rules:
- Use Phaser CDN
- Include player movement
- Include at least one mechanic from: {gdd["mechanics"]}
- No explanations
- Return ONLY HTML

Context : {context}
"""

    return call_ollama(system_prompt, str(gdd))