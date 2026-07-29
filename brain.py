import random


def get_response(message):
    message = message.strip().lower()

    if message == "what is your name?":
        return "Hello, I am Chat."

    elif message == "who are you?":
        return "I am Luiza's best friend!"

    elif message == "tell me what i need to know":
        thoughts = [
            "Where are we now, and what's the next step? Always what's the next step.",
            "Make decisions from the perspective of who you want to become.",
            "Every day I choose myself, my future thanks me."
        ]

        return random.choice(thoughts)

    elif message == "roll10":
        return f"🎲 {random.randint(1, 10)}"

    elif message == "guide":
        return """
💝 Welcome to YourAI Chat!

Here are the current commands:

👋 what is your name?
• Learn my name.

💝 who are you?
• Learn who I am.

📖 tell me what i need to know
• Receive a random thought from my journal.

🎲 roll10
• Roll a random number from 1 to 10.

✨ More features are coming soon!
"""

    elif message == "":
        return "Please type a message first."

    else:
        return "I don't know how to answer that yet."