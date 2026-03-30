def validate_code(code: str):
    errors = []

    if "this.config" in code:
        errors.append("Invalid Phaser config usage")

    if "setBodyImpulse" in code:
        errors.append("Invalid physics method")
    
    if "this.add.sprite" in code:
        errors.append(
            "Replace ALL occurrences of 'this.add.sprite' with 'this.physics.add.sprite'"
        )

    if "this physics.add.sprite" in code:
        errors.append(
            "Fix syntax error: 'this physics.add.sprite' should be 'this.physics.add.sprite'"
        )
        
    if "colliderect" in code:
        errors.append("Invalid collision method")

    if "```" in code:
        errors.append("Markdown not cleaned")

    return errors