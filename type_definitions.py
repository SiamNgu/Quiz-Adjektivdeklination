from typing import TypedDict, Literal, Protocol
from abc import abstractmethod

type JsonObject = dict[JsonObject] | str | int | float | bool
type JsonFile = dict[JsonObject]


class Params(TypedDict):
    case: Literal["nominativ", "akkusativ", "dativ", "genitiv"]
    gender: Literal["maskulin", "feminin", "neutral"]
    number: Literal["singular", "plural"]
    person: Literal["1", "2", "3"]


# --- Function protocol ---
class GetCorrectAnswerFn(Protocol):
    def __call__(params: Params, data: JsonFile) -> str: ...


class GrammarUtil:
    @staticmethod
    @abstractmethod
    def get_correct_answer(params: Params, data: JsonFile) -> str:
        pass
