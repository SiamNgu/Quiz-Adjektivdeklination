from random import choice
from json import load, dumps
from type_definitions import Params, GetCorrectAnswerFn


def open_json(path):
    with open(path) as file:
        return load(file)


def generate_params(categories: dict[str, list[str]]) -> Params:
    return {category[0]: choice(category[1]) for category in categories.items()}


def start_quiz(
    steps: int,
    data_path: str,
    get_correct_answer: GetCorrectAnswerFn,
) -> None:
    data = open_json(data_path)
    categories = open_json("categories.json")

    for n in range(steps):
        params = generate_params(categories=categories)
        correct_answer = get_correct_answer(params=params, data=data)

        user_input = str(
            input("Question no." + str(n) + (dumps(params, indent=2) + "\n"))
        )

        if user_input == "q" or user_input == "quit":
            return

        elif correct_answer == user_input:
            print("✔️")

        else:
            print(f"❌\ncorrect answer is {correct_answer}")

        print(f"\n{'-'*20}")


from possessiv_pronomen.possessiv_pronomen_endungen_util import PossessivPronomenUtil

start_quiz(
    steps=10,
    data_path="possessiv_pronomen/possessiv_pronomen_endungen.json",
    get_correct_answer=PossessivPronomenUtil.get_correct_answer,
)
