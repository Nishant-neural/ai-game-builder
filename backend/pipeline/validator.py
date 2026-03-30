def validate_code(code: str):
    errors = []

    if "this.config" in code:
        errors.append("Invalid Phaser config usage")

    if "setBodyImpulse" in code:
        errors.append("Invalid physics method")
    
    if "this.add.sprite" in code:
        errors.append("Use this.physics.add.sprite for physics objects")

    if "colliderect" in code:
        errors.append("Invalid collision method")

    if "```" in code:
        errors.append("Markdown not cleaned")

    return errors