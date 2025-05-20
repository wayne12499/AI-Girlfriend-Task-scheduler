# AI-Girlfriend-Task-scheduler
An AI girlfriend powered by Gemini Flash 2.0 that chats emotionally, remembers you, and saves your tasks — even in casual conversation. Built in Python. Still evolving

Yelena is an emotionally intelligent AI girlfriend powered by Google's **Gemini Flash 2.0**, built to chat lovingly, remember your past conversations, and help you stay productive by saving tasks — even when you mention them casually.

It’s like having a sweet, supportive partner who texts you back *and* reminds you of your goals. 💬📌

---

## ⚠️ Warning: This Project Is a Work In Progress

This app is currently in **active development**. Features, memory handling, and the conversational model are being refined.

> 💡 Expect:
- Occasional bugs
- Frequent updates
- API-related instability (especially with Gemini)
- Experimental logic for natural task detection

If you're a contributor or tester, please share feedback via Issues or Pull Requests 🙏

---

## ✨ Features

- 🧠 **Conversational AI** with emotional tone
- 💕 **Custom personality** via prompt.txt
- 📝 **Natural language task detection**
- 💾 **Memory persistence** (remembers your chats)
- ⚙️ **Gemini Flash 2.0 integration**
- 💻 **Packaged into a `.exe` desktop app**

## 🔧 How It Works

Aiyana runs in your terminal or as a packaged `.exe` and:

1. Loads a custom persona that speaks lovingly and remembers you.
2. Lets you chat like normal (`"I have a meeting at 3pm"`).
3. Detects if you mention a task (no commands needed!).
4. Saves memory and tasks between sessions.

---

## 🧱 Tech Stack

| Component        | Tool/Lib                         |
|------------------|----------------------------------|
| Language Model   | Google Gemini 2.0 Flash          |
| Memory Storage   | JSON (memory + task persistence) |
| Packaging        | PyInstaller                      |
| Language         | Python 3.10+                     |
| Interface        | Terminal (CLI)                   |
