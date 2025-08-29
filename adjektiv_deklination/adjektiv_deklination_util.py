from type_definitions import GrammarUtil


class AdjektivDeklinationUtil(GrammarUtil):
    @staticmethod
    def get_correct_answer(params, data):
        return data[params["artikel"]][params["case"]][
            params["gender"] if params["number"] == "singular" else params["number"]
        ]
