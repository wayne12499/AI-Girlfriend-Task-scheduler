import yaml
import codecs
import sys
import os
import google.generativeai as genai
from utils.memory_manager import load_memory, save_memory, remember_message
from utils.scheduler import add_task, show_tasks

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

with open(resource_path("config.yaml"), "r") as f:
    config = yaml.safe_load(f)

    genai.configure(api_key=config["gemini_api_key"])

    AI_NAME = config["ai_name"]
    USER_NAME = config["user_name"]
    model = genai.GenerativeModel("gemini-2.0-flash")

def chat_with_ai(prompt, memory):
    with codecs.open(resource_path('persona/prompt.txt'), 'r', encoding='utf-8', errors='ignore') as f:
        system_prompt = f.read()

    full_prompt = f"{system_prompt}\n\n{USER_NAME}: {prompt}"
    history = [
        {"role": "user", "parts": m["user"]} if i % 2 == 0 else {"role": "model", "parts": m["ai"]}
        for i, m in enumerate(memory[-5:])
        for _ in (0, 1)
        ]

    chat = model.start_chat(history=history)
    response = chat.send_message(full_prompt)
    return response.text.strip()

if __name__ == "__main__":
    memory = load_memory()
    print(f"{AI_NAME}: Hey love! 💖 I'm here for you — tell me anything.")

    while True:
        try:
            user_input = input(f"{USER_NAME}: ")
            if user_input.lower() in ["exit", "quit", "bye"]:
                print(f"{AI_NAME}: Okay babe, talk to you soon 💕")
                break

            if user_input.lower().startswith("show tasks"):
                tasks = show_tasks()
                print(f"{AI_NAME}: Here are your tasks:\n" + "\n".join(tasks))

            else:
                reply = chat_with_ai(user_input, memory)
                print(f"{AI_NAME}: {reply}")
                remember_message(memory, user_input, reply)

                task_keywords = ["remind me to", "i need to", "don't forget to", "i have to", "schedule", "set a reminder", "make sure to"]
                if any(keyword in user_input.lower() for keyword in task_keywords):
                    add_task(user_input)
                    print(f"{AI_NAME}: Got it, I saved that task for you 💕")

                save_memory(memory)

        except KeyboardInterrupt:
            print(f"\n{AI_NAME}: Bye babe! 💖")
            break
