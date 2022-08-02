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
    json = requests.get(
        f"{DOMAIN}/{TABLE}/filter/",
        params={
            f"select": "{TABLE}_cit,{TABLE}_freq_rank123,{TABLE}_len",
            "top": str(n),
            f"{TABLE}_len__ge": str(get_len()),
            f"{TABLE}_freq_rank123__ge": str(get_rank())
            if parameters.type_frequency
            else "",
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
