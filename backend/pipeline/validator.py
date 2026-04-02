from pipeline.llm_validator import llm_validate

def validate_code(code: str):
    errors = []

    errors += check_syntax(code)
    errors += check_phaser_api(code)
    errors += check_structure(code)
    errors += check_logic(code)
    llm_errors = llm_validate(code)

    
    errors += llm_errors

    return list(set(errors))
    

def check_syntax(code: str):
    errors = []

    if "```" in code:
        errors.append("Remove markdown formatting")

    if "<html" not in code.lower():
        errors.append("Missing HTML structure")

    if "new Phaser.Game" not in code:
        errors.append("Missing Phaser game initialization")

    if "scene:" not in code:
        errors.append("Game config missing scene assignment")

    if "preload(" not in code:
        errors.append("Missing preload function for assets")

    if "this.cursors" in code and "createCursorKeys" not in code:
        errors.append("cursors used but not initialized")

    return errors

def check_phaser_api(code: str):
    errors = []


    if "this.matter" in code and "this.physics" in code:
        errors.append("Do not mix Matter and Arcade physics")

    
    if "this.add.sprite" in code:
        errors.append("Use this.physics.add.sprite for game objects")

    
    if "setBodyImpulse" in code:
        errors.append("Invalid API: setBodyImpulse")

    if "colliderect" in code:
        errors.append("Invalid API: colliderect")

    if "cache-manager" in code:
        errors.append("Invalid Phaser API: cache-manager")

    return errors

def check_structure(code: str):
    errors = []

    
    if "class" not in code and "scene:" not in code:
        errors.append("No scene defined")

    
    if "scene:" in code and "class" in code:
        scene_index = code.find("scene:")
        class_index = code.find("class")

        if scene_index < class_index:
            errors.append("Scene defined after config (wrong order)")


    if "create(" not in code:
        errors.append("Missing create function")

    if "update(" not in code:
        errors.append("Missing update function")

    return errors

def check_logic(code: str):
    errors = []

    
    if "bird" in code and "physics.add.sprite" not in code:
        errors.append("Game object 'bird' missing physics")

    
    if "pipes" in code and "sprite" not in code:
        errors.append("Pipes are not created as sprites")


    if "Phaser.Math.Vector2" in code:
        errors.append("Using Vector2 instead of sprite object")

    
    if "score" in code and "setText" not in code:
        errors.append("Score not updated properly")

    return errors