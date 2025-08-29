from random import choice
from json import load, dumps
from type_definitions import Params, GetCorrectAnswerFn


def open_json(path):
    with open(path) as file:
        return load(file)

def table_print(data)

def generate_params(categories: dict[str, list[str]]) -> Params:
    return {category[0]: choice(category[1]) for category in categories.items()}


def start_quiz(
    steps: int,
    data_path: str,
    get_correct_answer: GetCorrectAnswerFn,
) -> None:
    data = open_json(data_path)
    categories = open_json("categories.json")
    correct_answer_count = 0

    for n in range(steps):
        params = generate_params(categories=categories)
        correct_answer = get_correct_answer(data=data, correct_answer=correct_answer)

        user_input = str(
            input("Question no." + str(n) + "\n" + (dumps(params, indent=2) + "\n"))
        )

        if user_input == "q" or user_input == "quit":
            return

        elif correct_answer == user_input:
            correct_answer_count += 1
            print("✔️")

        else:
            print(f"❌\ncorrect answer is {correct_answer}")

        if n == (steps - 1):
            print(f"Quiz complete: {correct_answer_count}/{steps}")

        print(f"\n{'-'*20}")


from possessiv_pronomen.possessiv_pronomen_endungen_util import PossessivPronomenUtil
from adjektiv_deklination.adjektiv_deklination_util import AdjektivDeklinationUtil


start_quiz(
    steps=10,
    data_path="adjektiv_deklination/adjektiv_deklination_data.json",
    get_correct_answer=AdjektivDeklinationUtil.get_correct_answer,
)
