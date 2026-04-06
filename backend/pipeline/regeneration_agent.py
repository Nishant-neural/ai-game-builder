from utility.utils import call_ollama
def regenerate_code(gdd, errors):
    system_prompt = f"""
You are a Phaser 3 expert.

The previous code is structurally broken.

Rebuild the game from scratch.

STRICT RULES:
- Use Phaser 3 arcade physics
- Use this.physics.add.sprite
- Define scene BEFORE config
- Include preload, create, update
- No explanations
- Return ONLY HTML

Avoid these errors:
{errors}
"""

    return call_ollama(system_prompt, str(gdd))