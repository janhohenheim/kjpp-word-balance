from itertools import repeat
from typing import List
import requests
import random
from kjpp_word_balance.model import Parameters, ViewModel

DOMAIN = "http://dlexdb.de/sr/dlexdb/kern"
"http://dlexdb.de/sr/dlexdb/kern/lem/filter/?select=lem_cit,lem_freq_abs,lem_len&order_by=typ_freq_abs&top=20&skip=0&top=&skip=&lem_len__ge=das"


def get_words(view_model: ViewModel) -> List[List[str]]:
    words = [[] for _ in range(view_model.condition_count)]
    for _ in range(view_model.word_count):
        similar_words = get_words_in_condition(
            view_model.parameters, view_model.condition_count
        )
        words.append(similar_words)
    return words


def get_words_in_condition(parameters: Parameters, n: int) -> List[str]:
    json = requests.get(
        f"{DOMAIN}/lem/filter/",
        params={
            "select": "lem_cit,lem_freq_rank123,lem_len",
            "top": str(n),
            "lem_len__ge": str(get_len()),
            "lem_freq_rank123__ge": str(get_rank())
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
