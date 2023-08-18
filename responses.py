import random


def get_response(message):
    p_message = message.lower()
    mobile_games = ["Fate Grand Order", "Candy Crush", "Angry Birds", "Temple Run",
                    "World of Tanks Blitz", "Please Touch Some Grass"]
    if p_message == "!recommend":
        recommended_game = random.choice(mobile_games)
        return recommended_game

    if p_message == "hello":
        return "Hello there!"

    if message == "roll":
        return str(random.randint(1, 6))

    if p_message == "!help":
        return "`Type !recommend to receive a suggestion from our lovely bot. Results may vary.`"

    return "I don't understand what you wrote."
