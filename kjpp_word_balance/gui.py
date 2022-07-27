import dearpygui.dearpygui as dpg
from word_generation import generate_words
from model import ViewModel, Parameters


def generate_view_model() -> ViewModel:
    return ViewModel(
        word_count=dpg.get_value("__input_word_count"),
        condition_count=dpg.get_value("__input_condition_count"),
        parameters=Parameters(
            param_one=dpg.get_value("__input_param_one"),
            param_two=dpg.get_value("__input_param_two"),
        ),
    )


def on_generate_words_clicked():
    view_model = generate_view_model()
    generate_words(view_model)


def create_gui():
    dpg.create_context()
    with dpg.window(tag="Primary Window"):

        dpg.add_button(
            label="Wortliste generieren", callback=on_generate_words_clicked, indent=50
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
