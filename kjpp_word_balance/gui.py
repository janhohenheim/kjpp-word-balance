import dearpygui.dearpygui as dpg
from kjpp_word_balance.network import get_words
from kjpp_word_balance.model import ViewModel, Parameters


def generate_view_model() -> ViewModel:
    return ViewModel(
        word_count=dpg.get_value("__input_word_count"),
        condition_count=dpg.get_value("__input_condition_count"),
        parameters=Parameters(
            grapheme_number=dpg.get_value("__input_grapheme_number"),
            sillable_number=dpg.get_value("__input_sillable_number"),
            sillable_frequency=dpg.get_value("__input_sillable_frequency"),
            bigram_frequency=dpg.get_value("__input_bigram_frequency"),
            type_frequency=dpg.get_value("__input_type_frequency"),
            phoneme_frequency=dpg.get_value("__input_phoneme_frequency"),
        ),
    )


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
        dpg.add_text("Balanciere Wörter nach:")
        with dpg.table(header_row=False):
            dpg.add_table_column(label="Kondition")
            dpg.add_table_column(label="Wortanzahl")
            with dpg.table_row():
                dpg.add_checkbox(
                    label="Graphemanzahl",
                    default_value=True,
                    tag="__input_grapheme_number",
                )

                dpg.add_checkbox(
                    label="Silbenanzahl",
                    default_value=True,
                    tag="__input_sillable_number",
                )
            with dpg.table_row():
                dpg.add_checkbox(
                    label="Silbenfrequenz",
                    default_value=True,
                    tag="__input_sillable_frequency",
                )

                dpg.add_checkbox(
                    label="Bigramfrequenz",
                    default_value=True,
                    tag="__input_bigram_frequency",
                )

            with dpg.table_row():
                dpg.add_checkbox(
                    label="Typfrequenz",
                    default_value=True,
                    tag="__input_type_frequency",
                )

                dpg.add_checkbox(
                    label="Phonemfrequenz",
                    default_value=True,
                    tag="__input_phoneme_frequency",
                )

    dpg.create_viewport(title="Word Balance", width=300, height=400)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()
