import dearpygui.dearpygui as dpg
from kjpp_word_balance.network import RangeError
from kjpp_word_balance.word_generation import RestrictionError, generate_words
from kjpp_word_balance.model import *
from kjpp_word_balance.gui_creation import *


def on_generate_words_clicked():
    with dpg.window(label="Wörter", width=700, height=400):

        view_model = generate_view_model()
        try:
            words = generate_words(view_model)
            with dpg.table(header_row=True, row_background=True):
                for i in range(view_model.condition_count):
                    dpg.add_table_column(label=f"Kategorie {i + 1}")
                for category in words:
                    with dpg.table_row():
                        for word in category:
                            dpg.add_text(word)
        except RestrictionError:
            dpg.add_text(
                "Es konnten nicht genug Wörter mit den angegebenen Einstellungen generiert werden.\nSenke bitte die Einschränkungen und versuche es erneut."
            )

        except RangeError:
            dpg.add_text(
                "Die angegebene Typfrequenzrange ist ungültig oder zu klein.\nBitte passe sie an und versuche es erneut."
            )


def create_gui():
    dpg.create_context()
    fonts = load_fonts()
    with dpg.window(tag="Primary Window"):
        dpg.add_text("Einstellungen")
        add_number_input("Anzahl Wörter per Kondition", "word_count", 20)
        add_number_input("Anzahl Konditionen", "condition_count", 4)
        add_text_input("Unerlaubte Buchstaben", "blacklisted_symbols", "äöü")
        add_text_input("Erlaubte Typfrequenz", "type_frequency_range", "1-2000")
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
