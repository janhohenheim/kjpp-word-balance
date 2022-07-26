#!/usr/bin/env python3
from typing import List
import dearpygui.dearpygui as dpg
from dataclasses import dataclass


class Parameters:
    param_one: bool = True
    param_two: bool = False


class ViewModel:
    word_count: int = 0
    condition_count: int = 0
    parameters: Parameters


def generate_callback():
    print("Save Clicked")


def main():
    dpg.create_context()
    view_model = ViewModel()
    with dpg.window(tag="Primary Window"):
        dpg.add_button(
            label="Wortliste generieren",
            user_data=view_model,
            callback=generate_callback,
        )
        view_model.word_count = dpg.add_input_int(
            label="Anzahl Wörter per Kondition", default_value=10
        )
        view_model.condition_count = dpg.add_input_int(
            label="Anzahl Konditionen", default_value=1
        )
        dpg.add_text("Parameter")
        with dpg.table(header_row=False):
            dpg.add_table_column(label="Kondition")
            dpg.add_table_column(label="Wortanzahl")
            with dpg.table_row():
                view_model.parameters.param_one = dpg.add_checkbox(
                    label="Kondition 1", default_value=True
                )
                view_model.parameters.param_two = dpg.add_checkbox(
                    label="Kondition 2", default_value=True
                )
    dpg.create_viewport(title="Word Balance", width=400, height=800)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
