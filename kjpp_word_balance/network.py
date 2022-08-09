from dataclasses import dataclass
from typing import Dict, List
import requests
import random
from kjpp_word_balance.model import ViewModel

DOMAIN = "http://dlexdb.de/sr/dlexdb/kern"
TABLE = "typ"

class RangeError(Exception):
    pass

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
    n: int, view_model: ViewModel, blacklisted_words: List[str]
) -> Dict[str, List[int]]:
    columns = Columns()
    column_selector = ",".join([column for column in columns.iter()])

    n = n * random.randint(2, 10)
    range = get_range(view_model, n)
    word_regex = generate_word_regex(view_model.blacklisted_symbols, blacklisted_words)

    json = requests.get(
        f"{DOMAIN}/{TABLE}/filter/",
        params={
            f"select": column_selector,
            "top": str(n),
            f"{columns.grapheme_number}__ge": 3,
            f"{columns.grapheme_number}__le": 12,
            f"{columns.type_frequency}__ge": range[0],
            f"{columns.type_frequency}__le": range[1],
            f"{columns.word}__eq": word_regex,
        },
        headers={"Accept": "application/json"},
    ).json()
    words = json["data"]
    return {word[0]: word[1:] for word in words}


def generate_word_regex(
    blacklisted_symbols: List[str], blacklisted_words: List[str]
) -> str:
    capitalized_blacklisted_words = [word.capitalize() for word in blacklisted_words]

    blacklisted_symbols = "".join(blacklisted_symbols)
    blacklisted_symbols = blacklisted_symbols.lower() + blacklisted_symbols.upper()
    blacklisted_words = "".join(
        f"(?!{word})" for word in blacklisted_words + capitalized_blacklisted_words
    )

    default_blacklist = "0-9\.,\-\_'?!"
    return f"/^{blacklisted_words}[^{default_blacklist}{blacklisted_symbols}]{{3,}}$/"


def get_range(view_model: ViewModel, n: int) -> int:
    max = view_model.type_frequency_range[1]
    min = view_model.type_frequency_range[0]
    try:
        lower = random.randint(min, max - n)
        return lower, max
    except ValueError:
        raise RangeError
