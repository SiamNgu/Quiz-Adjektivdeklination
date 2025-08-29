from type_definitions import GrammarUtil


class PersonalPronomenUtil(GrammarUtil):
    @staticmethod
    def get_correct_answer(params, data):
        return (
            data[params["number"]][params["person"]][params["case"]][params["gender"]]
            if params["number"] == "singular" and params["person"] == "3"
            else data[params["number"]][params["person"]][params["case"]]
        )
