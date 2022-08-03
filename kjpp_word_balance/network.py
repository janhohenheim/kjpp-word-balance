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


def fetch_at_least_n_random_words(
    n: int, view_model: ViewModel
) -> Dict[str, List[int]]:
    columns = Columns()
    column_selector = ",".join([column for column in columns.iter()])
    n = n * random.randint(2, 10)
    blacklisted_symbols = "".join(view_model.blacklisted_symbols)
    blacklisted_symbols = blacklisted_symbols.lower() + blacklisted_symbols.upper()
    default_blacklist = "0-9\.,\-\_'?!"
    json = requests.get(
        f"{DOMAIN}/{TABLE}/filter/",
        params={
            f"select": column_selector,
            "top": str(n),
            f"{columns.grapheme_number}__ge": 3,
            f"{columns.grapheme_number}__le": 12,
            f"{columns.type_frequency}__ge": str(get_random_rank()),
            f"{columns.word}__eq": f"/^[^{default_blacklist}{blacklisted_symbols}]{{3,}}$/",
        },
        headers={"Accept": "application/json"},
    ).json()
    words = json["data"]
    return {word[0]: word[1:] for word in words}


def get_random_rank():
    return random.choice(range(100, 5_000))
