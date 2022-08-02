from typing import List
import requests
import random
from kjpp_word_balance.model import Parameters, ViewModel

DOMAIN = "http://dlexdb.de/sr/dlexdb/kern"


def get_words(view_model: ViewModel) -> List[List[str]]:
    words = [[] for _ in range(view_model.condition_count)]
    for _ in range(view_model.word_count):
        similar_words = get_words_in_condition(
            view_model.parameters, view_model.condition_count
        )
        words.append(similar_words)
    return words


def get_words_in_condition(parameters: Parameters, n: int) -> List[str]:
    TABLE = "typ"
    word_column = f"{TABLE}_cit"
    filter_columns = ",".join(
        [
            f"{TABLE}_{parameter.api_column}"
            for parameter in parameters.__dict__.values()
            if parameter.api_column != ""
        ]
    )
    json = requests.get(
        f"{DOMAIN}/{TABLE}/filter/",
        params={
            f"select": f"{word_column},{filter_columns}",
            "top": str(n),
            f"{TABLE}_{parameters.grapheme_number.api_column}__ge": str(get_len()),
            f"{TABLE}_{parameters.type_frequency.api_column}__ge": str(get_rank()),
            f"{word_column}__eq": "/^\\w{3,}$/",
        },
        headers={"Accept": "application/json"},
    ).json()
    filters = json["data"]
    words = [filters[0] for filters in filters]
    if len(words) != n:
        return get_words_in_condition(parameters, n)
    return words


def get_len():
    return random.choice(range(3, 10))


def get_rank():
    return random.choice(range(100, 2000))
