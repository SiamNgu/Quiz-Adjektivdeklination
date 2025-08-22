import random

def request_answer():
    # Define the grammatical categories
    cases = ["Nominativ", "Akkusativ", "Dativ", "Genitiv"]
    # Added "Neutral" for completeness
    genders = ["Maskulin", "Feminin", "Neutral", "Plural"]
    # "Artikel" (article type) is crucial for adjective endings
    artikels = ["Null", "Bestimmten", "Unbestimmten"]

    # --- Adjective Ending Rules Data Structure ---
    # This dictionary holds all the rules for German adjective declension.
    endings = {
        # No article (strong declension)
        "Null": {
            "Nominativ": {"Maskulin": "er", "Feminin": "e", "Neutral": "es", "Plural": "e"},
            "Akkusativ": {"Maskulin": "en", "Feminin": "e", "Neutral": "es", "Plural": "e"},
            "Dativ": {"Maskulin": "em", "Feminin": "er", "Neutral": "em", "Plural": "en"},
            "Genitiv": {"Maskulin": "en", "Feminin": "er", "Neutral": "en", "Plural": "er"}
        },
        # Definite article (weak declension)
        "Bestimmten": {
            "Nominativ": {"Maskulin": "e", "Feminin": "e", "Neutral": "e", "Plural": "en"},
            "Akkusativ": {"Maskulin": "en", "Feminin": "e", "Neutral": "e", "Plural": "en"},
            "Dativ": {"Maskulin": "en", "Feminin": "en", "Neutral": "en", "Plural": "en"},
            "Genitiv": {"Maskulin": "en", "Feminin": "en", "Neutral": "en", "Plural": "en"}
        },
        # Indefinite article (mixed declension)
        "Unbestimmten": {
            "Nominativ": {"Maskulin": "er", "Feminin": "e", "Neutral": "es", "Plural": "en"},
            "Akkusativ": {"Maskulin": "en", "Feminin": "e", "Neutral": "es", "Plural": "en"},
            "Dativ": {"Maskulin": "en", "Feminin": "en", "Neutral": "en", "Plural": "en"},
            "Genitiv": {"Maskulin": "en", "Feminin": "en", "Neutral": "en", "Plural": "en"}
        }
    }

    # --- Quiz Logic ---

    # Randomly select the parameters for the question
    case = random.choice(cases)
    gender = random.choice(genders)
    artikel = artikels[2]

    # Determine the correct answer using the dictionary
    # The keys are used to navigate the nested dictionary to find the ending.
    correct_answer: str = endings[artikel][case][gender]

    # Print the question to the user
    print("_____________________________"*2)
    print(f"Artikel: {artikel}, Case: {case}, Gender: {gender}")
    user_input = str(input("What is the adjective ending? -> "))

    # Check the user's answer (strip whitespace and convert to lower case for leniency)
    if user_input == 'q' or user_input == 'quit':
        return user_input
    elif user_input.strip().lower() == correct_answer:
        print(f"\nCorrect! ✅ The ending is '-{correct_answer}'.")
    else:
        print(f"\nIncorrect. ❌ The correct ending was '-{correct_answer}'.")
    print()
    return user_input


while True:
    output = request_answer()
    if output == "q" or output == "quit":
        break
