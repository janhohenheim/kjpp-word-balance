from typing import Dict, List


def take_most_similar_words(
    words: Dict[str, List[int]], n: int, weights: List[float]
) -> List[str]:
    words = normalize_scores(words)
    words = convert_scores_to_mean_squared_error(words)
    words = get_weighted_sum_of_squares(words, weights)
    words = sorted(words, key=lambda word: words[word])
    return [word.replace("ß", "ss").lower() for word in words[0:n]]


def get_weighted_sum_of_squares(
    words: Dict[str, List[float]],
    weights: List[float],
) -> Dict[str, float]:
    return {
        word: sum(error * weight for error, weight in zip(errors, weights))
        for word, errors in words.items()
    }


def convert_scores_to_mean_squared_error(
    words: Dict[str, List[float]]
) -> Dict[str, List[float]]:
    means = get_mean_scores(words)
    return {
        word: [(score - mean) ** 2 for score, mean in zip(scores, means)]
        for word, scores in words.items()
    }


def get_mean_scores(words: Dict[str, List[float]]) -> List[float]:
    scores_per_word = get_scores_per_word(words)
    return [
        sum(scores[n] for scores in words.values()) / len(words)
        for n in range(scores_per_word)
    ]


def normalize_scores(words: Dict[str, List[int]]) -> Dict[str, List[float]]:
    max_scores = get_max_scores(words)
    return {
        word: [
            float(score) / float(max_score)
            for score, max_score in zip(scores, max_scores)
        ]
        for word, scores in words.items()
    }


def get_max_scores(words: Dict[str, List[int]]) -> List[int]:
    scores_per_word = get_scores_per_word(words)
    return [max(scores[n] for scores in words.values()) for n in range(scores_per_word)]


def get_scores_per_word(words: Dict[str, List[int]]) -> int:
    return len(words.values().__iter__().__next__())
