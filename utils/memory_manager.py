import json
import os

LOCAL_MEMORY_FILE = os.path.join(os.getcwd(), "memory_memory.json")

def load_memory():
    if not os.path.exists(LOCAL_MEMORY_FILE):
        return []
    with open(LOCAL_MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(memory):
    with open(LOCAL_MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def remember_message(memory, user_input, ai_response):
    memory.append({
        "user": user_input,
        "ai": ai_response
    })
