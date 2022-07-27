from dataclasses import dataclass


@dataclass(frozen=True)
class Parameters:
    param_one: bool
    param_two: bool


@dataclass(frozen=True)
class ViewModel:
    word_count: int
    condition_count: int
    parameters: Parameters
