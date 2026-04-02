import json
import os

MEMORY_FILE = "memory/memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {"errors": [], "fixes": []}

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)


def add_error(memory, error):
    if error not in memory["errors"]:
        memory["errors"].append(error)


def add_fix(memory, fix):
    if fix not in memory["fixes"]:
        memory["fixes"].append(fix)