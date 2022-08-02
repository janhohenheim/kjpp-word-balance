import dearpygui.dearpygui as dpg
from kjpp_word_balance.network import get_words
from kjpp_word_balance.model import *
from kjpp_word_balance.gui_creation import *


def on_generate_words_clicked():
    view_model = generate_view_model()
    words = get_words(view_model)
    with dpg.window():
        with dpg.table():
            for i in range(view_model.condition_count):
                dpg.add_table_column(label=f"Kategorie {i + 1}")
            for category in words:
                with dpg.table_row():
                    for word in category:
                        dpg.add_text(word)


def create_gui():
    dpg.create_context()
    with dpg.window(tag="Primary Window"):

        dpg.add_button(
            label="Wortliste generieren", callback=on_generate_words_clicked, indent=50
        )
        dpg.add_spacer(height=2)

        add_number_input("Anzahl Wörter per Kondition", "word_count")
        add_number_input("Anzahl Konditionen", "condition_count")

        dpg.add_text("Balanciere Wörter nach:")
        with dpg.table(header_row=False):
            dpg.add_table_column(label="Kondition")
            dpg.add_table_column(label="Wortanzahl")
            with dpg.table_row():
                add_parameter_input("Graphemalzahl", "grapheme_number")
                add_parameter_input("Sillabelzahl", "sillable_number")
            with dpg.table_row():
                add_parameter_input("Silbenfrequenz", "sillable_frequency")
                add_parameter_input("Bigrammfrequenz", "bigram_frequency")

            with dpg.table_row():
                add_parameter_input("Typfrequenz", "type_frequency")
                add_parameter_input("Phonemefrequenz", "phoneme_frequency")

    dpg.create_viewport(title="Word Balance", width=300, height=400)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()
