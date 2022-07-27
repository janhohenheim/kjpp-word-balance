#!/usr/bin/env python3
from subprocess import call
from typing import List
import dearpygui.dearpygui as dpg
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


def generate_view_model() -> ViewModel:
    return ViewModel(
        word_count=dpg.get_value("__input_word_count"),
        condition_count=dpg.get_value("__input_condition_count"),
        parameters=Parameters(
            param_one=dpg.get_value("__input_param_one"),
            param_two=dpg.get_value("__input_param_two"),
        ),
    )


def main():
    dpg.create_context()
    with dpg.window(tag="Primary Window"):

        def generate_callback():
            view_model = generate_view_model()
            print("Generate button clicked")
            print(f"Word count: {view_model.word_count}")
            print(f"Condition count: {view_model.condition_count}")
            print(f"Parameters:")
            print(f"  param_one: {view_model.parameters.param_one}")
            print(f"  param_two: {view_model.parameters.param_two}")

        dpg.add_button(
            label="Wortliste generieren", callback=generate_callback, indent=50
        )
        dpg.add_spacer(height=2)

        dpg.add_input_int(
            label="Anzahl Wörter per Kondition",
            default_value=10,
            min_value=1,
            max_value=100,
            width=80,
            min_clamped=True,
            max_clamped=True,
            tag="__input_word_count",
        )

        dpg.add_input_int(
            label="Anzahl Konditionen",
            default_value=1,
            min_value=1,
            max_value=100,
            width=80,
            min_clamped=True,
            max_clamped=True,
            tag="__input_condition_count",
        )
        dpg.add_text("Parameter")
        with dpg.table(header_row=False):
            dpg.add_table_column(label="Kondition")
            dpg.add_table_column(label="Wortanzahl")
            with dpg.table_row():
                dpg.add_checkbox(
                    label="Kondition 1",
                    default_value=True,
                    tag="__input_param_one",
                )

                dpg.add_checkbox(
                    label="Kondition 2",
                    default_value=True,
                    tag="__input_param_two",
                )
    dpg.create_viewport(title="Word Balance", width=300, height=400)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
