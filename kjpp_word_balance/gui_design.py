import dearpygui.dearpygui as dpg
from kjpp_word_balance.network import get_words
from kjpp_word_balance.model import *
from kjpp_word_balance.gui_creation import *


def on_generate_words_clicked():
    view_model = generate_view_model()
    words = get_words(view_model)

    with dpg.window(label="Wörter", width=700, height=400):
        with dpg.table():
            for i in range(view_model.condition_count):
                dpg.add_table_column(label=f"Kategorie {i + 1}")
            for category in words:
                with dpg.table_row():
                    for word in category:
                        dpg.add_text(word)


def create_gui():
    dpg.create_context()
    fonts = load_fonts()
    with dpg.window(tag="Primary Window"):
        dpg.add_text("Einstellungen")
        add_number_input("Anzahl Wörter per Kondition", "word_count")
        add_number_input("Anzahl Konditionen", "condition_count")

        dpg.add_spacer(height=5)
        dpg.add_text("Parametergewichtung (0 = ausgeschalten)")
        with dpg.table(header_row=False):
            dpg.add_table_column(label="Kondition")
            dpg.add_table_column(label="Wortanzahl")
            with dpg.table_row():
                add_parameter_input("Graphemanzahl", "grapheme_number")
                add_parameter_input("Silbenanzahl", "sillable_number")
            with dpg.table_row():
                add_parameter_input("Silbenfrequenz", "sillable_frequency")
                add_parameter_input("Bigrammfrequenz", "bigram_frequency")

            with dpg.table_row():
                add_parameter_input("Typfrequenz", "type_frequency")
                add_parameter_input("Phonemfrequenz", "phoneme_frequency")

        dpg.add_spacer(height=30)
        dpg.add_button(
            label="Wortliste generieren",
            callback=on_generate_words_clicked,
            indent=450,
        )
        dpg.bind_font(fonts.primary)

    dpg.create_viewport(title="Word Balance", width=700, height=400)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()
