from type_definitions import GrammarUtil


class PossessivPronomenUtil(GrammarUtil):
    @staticmethod
    def get_correct_answer(params, data):
        return data[params["case"]][
            params["gender"] if params["number"] == "singular" else params["number"]
        ]
