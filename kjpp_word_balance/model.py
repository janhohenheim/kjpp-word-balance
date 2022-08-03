import dearpygui.dearpygui as dpg
from dataclasses import dataclass


@dataclass(frozen=True)
class Parameter:
    weight: float
    api_column: str


@dataclass(frozen=True)
class Parameters:
    grapheme_number: Parameter
    sillable_number: Parameter
    sillable_frequency: Parameter
    bigram_frequency: Parameter
    type_frequency: Parameter
    phoneme_frequency: Parameter


@dataclass(frozen=True)
class ViewModel:
    word_count: int
    condition_count: int
    parameters: Parameters


@dataclass(frozen=True)
class Fonts:
    primary: str
    bold: str
