import random
from datetime import datetime
from pathlib import Path


journal_file = Path("journal.txt")
journal_unlocked = False


while True:
    original_message = input("You: ").strip()
    message = original_message.lower()

    if message == "933":
        journal_unlocked = True
        print("Chat: Journal access unlocked.")

    elif message == "what is your name?":
        print("Chat: Hello, I am Chat.")

    elif message == "who are you?":
        print("Chat: I am Luiza's best friend!")

    elif message == "tell me what i need to know":
        thoughts = [
            "Where are we now, and what's the next step? Always what's the next step.",
            "Make decisions from the perspective of who you want to become.",
            "Every day I choose myself, my future thanks me."
        ]

        chosen_thought = random.choice(thoughts)
        print("Chat:", chosen_thought)

    elif message == "journal entry":
        if journal_unlocked:
            entry = input("Chat: Tell me about your day:\nYou: ").strip()

            if entry == "":
                print("Chat: You didn't write anything, so I didn't save an entry.")

            else:
                date = datetime.now().strftime("%B %d, %Y")
                time = datetime.now().strftime("%I:%M %p")

                with journal_file.open("a", encoding="utf-8") as file:
                    file.write(f"Date: {date}\n")
                    file.write(f"Time: {time}\n")
                    file.write(f"Entry: {entry}\n")
                    file.write("---\n")

                print(f"Chat: I saved this memory from {date}.")

        else:
            print("Chat: This journal is private.")

    elif message == "what do you remember?":
        if journal_unlocked:
            if journal_file.exists():
                memories = journal_file.read_text(encoding="utf-8")

                if memories.strip() == "":
                    print("Chat: My journal is empty right now.")
                else:
                    print("Chat: Here is what I remember:\n")
                    print(memories)

            else:
                print("Chat: I don't have any journal entries yet.")

        else:
            print("Chat: This journal is private.")

    elif message.startswith("what do you remember from "):
        if journal_unlocked:
            requested_date = original_message[
                len("what do you remember from "):
            ].strip()

            if not journal_file.exists():
                print("Chat: I don't have any journal entries yet.")

            else:
                memories = journal_file.read_text(encoding="utf-8")
                entries = memories.split("---")
                matching_entries = []

                for entry in entries:
                    if requested_date.lower() in entry.lower():
                        matching_entries.append(entry.strip())

                if matching_entries:
                    print(f"Chat: I remember this from {requested_date}:\n")

                    for entry in matching_entries:
                        print(entry)
                        print()

                else:
                    print(f"Chat: I couldn't find a memory from {requested_date}.")

        else:
            print("Chat: This journal is private.")

    else:
        print("Chat: I don't know how to answer that yet.")