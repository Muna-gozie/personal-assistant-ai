project/
├── main.py                     # Entry point for local CLI version
├── webapp.py                   # Flask-based web API interface
├── requirements.txt            # All dependencies
├── core/
│   ├── llm.py                  # Interface to local/cloud LLM
│   ├── router.py               # Intent matching and skill dispatching
│   └── voice.py                # Speech-to-text and text-to-speech logic
├── skills/
│   ├── base.py                 # Abstract base for all skills
│   ├── system.py               # OS-level commands (open apps, etc.)
│   ├── time.py                 # Clock, reminders, alarms
│   ├── weather.py              # Weather report using OpenWeather API
│   └── fun.py                  # Jokes, small talk, Wikipedia
├── templates/
│   └── index.html              # Simple web UI (optional)
├── static/                     # CSS/JS for web interface (optional)
└── memory/
    └── memory.json             # Persistent memory (facts, context, user prefs)

# Sample: main.py
from core.router import route_command

while True:
    try:
        command = input("You: ")
        response = route_command(command)
        print("Assistant:", response)
    except KeyboardInterrupt:
        print("\nExiting...")
        break

# Sample: core/router.py
from skills import system, time, weather, fun
from difflib import get_close_matches

commands = {
    "open calculator": system.open_calculator,
    "what time is it": time.tell_time,
    # "weather in": weather.get_weather,
    # "tell me a joke": fun.tell_joke
}

def route_command(command: str):
    for key in commands:
        if key in command:
            return commands[key](command)
    return fun.ask_llm(command)  # fallback to LLM

# Sample: core/llm.py
import requests

def ask_llm(prompt: str):
    res = requests.post("http://localhost:11434/api/generate", json={"model": "mistral", "prompt": prompt})
    return res.json().get("response", "Sorry, I couldn’t understand that.")
