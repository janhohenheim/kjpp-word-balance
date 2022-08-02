from dataclasses import dataclass
from typing import Dict, List, Union
import requests
import random
from kjpp_word_balance.model import Parameters, ViewModel

DOMAIN = "http://dlexdb.de/sr/dlexdb/kern"
TABLE = "typ"


@dataclass(frozen=True)
class GenericColumns:
    word: str
    grapheme_number: str
    sillable_number: str
    sillable_frequency: str
    bigram_frequency: str
    type_frequency: str
    # phoneme_frequency: str


@dataclass(frozen=True)
class Columns(GenericColumns):
    def __init__(self, table: str = TABLE):
        super().__init__(
            word=f"{table}_cit",
            grapheme_number=f"{table}_len",
            sillable_number=f"{table}_syls_cnt",
            sillable_frequency=f"{table}_syls_cumfreq_token_rank123",
            bigram_frequency=f"{table}_init_bigr_rank123",
            type_frequency=f"{table}_freq_rank123",
        )

    def iter(self) -> List[str]:
        return super().__dict__.values()


def get_words(view_model: ViewModel) -> List[List[str]]:
    return [
        get_similar_words(view_model.condition_count, view_model.parameters)
        for _ in range(view_model.word_count)
    ]


def get_similar_words(n: int, parameters: Parameters) -> List[str]:
    words_with_ranks = get_random_words(n * 20)
    sorted_words_with_ranks = sorted(
        words_with_ranks, key=lambda word: get_weighted_score(word, parameters)
    )
    index = random.randint(0, len(sorted_words_with_ranks) - 1 - n)
    return [
        word[0].replace("ß", "ss").lower()
        for word in sorted_words_with_ranks[index : index + n]
    ]


def get_random_words(n: int) -> List[List[Union[int, str]]]:
    columns = Columns()
    column_selector = ",".join([column for column in columns.iter()])
    json = requests.get(
        f"{DOMAIN}/{TABLE}/filter/",
        params={
            f"select": column_selector,
            "top": str(n),
            f"{columns.grapheme_number}__ge": 3,
            f"{columns.grapheme_number}__le": 12,
            f"{columns.type_frequency}__ge": str(get_random_rank()),
            f"{columns.word}__eq": "/^\\w{3,}$/",
        },
        headers={"Accept": "application/json"},
    ).json()
    return json["data"]


def get_weighted_score(word: List[Union[(int, str)]], parameters: Parameters) -> int:
    scores = [int(score) for score in word[1:]]
    return sum(
        [
            score * int(parameter.weight)
            for score, parameter in zip(scores, parameters.__dict__.values())
            if parameter.api_column != ""
        ]
    )


def get_random_rank():
    return random.choice(range(100, 5_000))
