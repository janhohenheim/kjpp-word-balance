import dearpygui.dearpygui as dpg
from kjpp_word_balance.model import *
import pathlib
from os.path import join


def get_fonts_directory():
    code_path = pathlib.Path(__file__).parent.resolve()
    return join(code_path, "assets", "fonts")


def load_fonts() -> Fonts:
    fonts_path = get_fonts_directory()
    font_path = join(fonts_path, "Roboto", "Roboto-Regular.ttf")
    with dpg.font_registry():
        default_font = dpg.add_font(font_path, 24)
        second_font = dpg.add_font(font_path, 10)
    return Fonts(default_font, second_font)


def add_number_input(label: str, tag: str):
    dpg.add_input_int(
        label=label,
        default_value=10,
        min_value=1,
        max_value=100,
        width=120,
        min_clamped=True,
        max_clamped=True,
        tag=f"__input_{tag}",
    )


def add_parameter_input(label: str, tag: str):
    dpg.add_input_int(
        label=label,
        default_value=1,
        min_value=0,
        max_value=9,
        width=90,
        min_clamped=True,
        max_clamped=True,
        tag=f"__input_{tag}_weight",
    )


def generate_view_model() -> ViewModel:
    return ViewModel(
        word_count=dpg.get_value("__input_word_count"),
        condition_count=dpg.get_value("__input_condition_count"),
        parameters=Parameters(
            grapheme_number=Parameter(
                weight=dpg.get_value("__input_grapheme_number_weight"),
            ),
            sillable_number=Parameter(
                weight=dpg.get_value("__input_sillable_number_weight"),
            ),
            sillable_frequency=Parameter(
                weight=dpg.get_value("__input_sillable_frequency_weight"),
            ),
            bigram_frequency=Parameter(
                weight=dpg.get_value("__input_bigram_frequency_weight"),
            ),
            type_frequency=Parameter(
                weight=dpg.get_value("__input_type_frequency_weight"),
            ),
            phoneme_frequency=Parameter(
                weight=dpg.get_value("__input_phoneme_frequency_weight"),
            ),
        ),
    )
