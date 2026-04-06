from utility.utils import call_ollama
from rag.retreiver import retrieve_context

def generate_phaser_code(gdd: dict):
    context = retrieve_context(str(gdd))

    system_prompt = f"""
You are a Phaser 3 expert.

Generate a COMPLETE working Phaser game in ONE HTML file.
 You ONLY use these APIs:
- this.physics.add.sprite(x, y, key)
- this.physics.add.staticGroup()
- this.physics.add.collider(a, b)
- sprite.setVelocityY(n)
- this.cursors = this.input.keyboard.createCursorKeys()
- this.add.text(x, y, str, style)

NEVER use: setBodyImpulse, colliderect, this.add.sprite for physics objects,
Matter.js methods, or any Phaser 2 syntax.

Rules:
- Use Phaser CDN
- Include player movement
- Include at least one mechanic from: {gdd["mechanics"]}
- No explanations
- Output ONLY a complete single-file HTML document with no explanation.
- Start with <!DOCTYPE html>, end with </html>. No markdown. No backticks.

Context : {context}
"""

    return call_ollama(system_prompt, str(gdd))