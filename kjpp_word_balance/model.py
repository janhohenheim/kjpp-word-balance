from dataclasses import dataclass


@dataclass(frozen=True)
class Parameters:
    grapheme_number: bool
    sillable_number: bool
    sillable_frequency: bool
    bigram_frequency: bool
    type_frequency: bool
    phoneme_frequency: bool


@dataclass(frozen=True)
class ViewModel:
    word_count: int
    condition_count: int
    parameters: Parameters
