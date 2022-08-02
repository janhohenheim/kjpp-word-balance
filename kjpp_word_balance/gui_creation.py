import dearpygui.dearpygui as dpg
from kjpp_word_balance.model import *


def add_number_input(label: str, tag: str):
    dpg.add_input_int(
        label=label,
        default_value=10,
        min_value=1,
        max_value=100,
        width=80,
        min_clamped=True,
        max_clamped=True,
        tag=f"__input_{tag}",
    )


def add_parameter_input(name: str, tag: str):
    dpg.add_checkbox(
        label=name,
        default_value=True,
        tag=f"__input_{tag}_active",
    )


def generate_view_model() -> ViewModel:
    return ViewModel(
        word_count=dpg.get_value("__input_word_count"),
        condition_count=dpg.get_value("__input_condition_count"),
        parameters=Parameters(
            grapheme_number=Parameter(
                active=dpg.get_value("__input_grapheme_number_active"),
                weight=dpg.get_value("__input_grapheme_number_weight"),
            ),
            sillable_number=Parameter(
                active=dpg.get_value("__input_sillable_number_active"),
                weight=dpg.get_value("__input_sillable_number_weight"),
            ),
            sillable_frequency=Parameter(
                active=dpg.get_value("__input_sillable_frequency_active"),
                weight=dpg.get_value("__input_sillable_frequency_weight"),
            ),
            bigram_frequency=Parameter(
                active=dpg.get_value("__input_bigram_frequency_active"),
                weight=dpg.get_value("__input_bigram_frequency_weight"),
            ),
            type_frequency=Parameter(
                active=dpg.get_value("__input_type_frequency_active"),
                weight=dpg.get_value("__input_type_frequency_weight"),
            ),
            phoneme_frequency=Parameter(
                active=dpg.get_value("__input_phoneme_frequency_active"),
                weight=dpg.get_value("__input_phoneme_frequency_weight"),
            ),
        ),
    )
