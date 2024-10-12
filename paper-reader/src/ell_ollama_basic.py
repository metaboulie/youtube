import random

import ell
from openai import OpenAI

# use llama3.2:1b model
MODEL = "llama3.2"

# use ollama server
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)

# enable verbose mode
ell.config.verbose = True
# register the model
ell.config.register_model(MODEL, client)

# ell.init(store="./logdir", autocommit=True, verbose=True)


def get_random_adjective():
    """Returns a random adjective."""
    adjectives = [
        "enthusiastic",
        "cheerful",
        "warm",
        "friendly",
        "heartfelt",
        "sincere",
    ]
    return random.choice(adjectives)


def get_random_greeting():
    """Returns a random greeting."""
    greetings = [
        "Good night",
        "Goodbye",
        "See you soon",
        "Take care",
        "Have a great day",
        "Catch you later",
    ]
    return random.choice(greetings)


# let model introduce itself and greet the user with random adjective and greeting
@ell.simple(model=MODEL, client=client)
def greet(name: str):
    """You are a helpful and expressive assistant."""  # system prompt
    adjective = get_random_adjective()
    greeting = get_random_greeting()
    return f"Introduce your model version, and say a {adjective} {greeting} to {name}"  # user prompt


if __name__ == "__main__":
    while True:
        print("-" * 79)
        name = input("Your name: (type 'exit' to quit) ")
        if name.lower() == "exit":
            break
        greet(name)