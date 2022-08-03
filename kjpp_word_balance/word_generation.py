from typing import List
from kjpp_word_balance.model import ViewModel
from kjpp_word_balance.network import get_random_words
from kjpp_word_balance.similarity import take_most_similar_words


def generate_words(view_model: ViewModel) -> List[List[str]]:
    weights = [
        parameter.weight for parameter in view_model.parameters.__dict__.values()
    ]
    list_of_random_words = [
        get_random_words(view_model.condition_count * 20)
        for _ in range(view_model.word_count)
    ]
    return [
        take_most_similar_words(random_words, view_model.condition_count, weights)
        for random_words in list_of_random_words
    ]
