from typing import List
from kjpp_word_balance.model import ViewModel
from kjpp_word_balance.network import fetch_at_least_n_random_words
from kjpp_word_balance.similarity import take_most_similar_words
import random


def generate_words(view_model: ViewModel) -> List[List[str]]:
    weights = [
        parameter.weight for parameter in view_model.parameters.__dict__.values()
    ]
    list_of_words = []
    for _ in range(view_model.word_count):
        blacklisted_words = [word for words in list_of_words for word in words]
        random_words = fetch_at_least_n_random_words(
            view_model.condition_count, view_model, blacklisted_words
        )
        similar_words = take_most_similar_words(
            random_words, view_model.condition_count, weights
        )
        list_of_words.append(similar_words)
    return list_of_words
