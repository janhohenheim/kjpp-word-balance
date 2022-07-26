#!/usr/bin/env python3
import dearpygui.dearpygui as dpg
 

def generate_callback():
    print("Save Clicked")
 

def main():
    dpg.create_context()
 
    with dpg.window(tag="Primary Window"):
        dpg.add_button(label="Wortliste generieren", callback=generate_callback)
        word_count = dpg.add_input_int(
            label="Anzahl Wörter per Kondition", default_value=10
        )
        condition_count = dpg.add_input_int(label="Anzahl Konditionen", default_value=1)
        dpg.add_text("Parameter")
        with dpg.table(label="Parameter"):
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row():
                dpg.add_text("Kondition")
                dpg.add_text("Wörter")
    dpg.create_viewport(title="Word Balance", width=400, height=800)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()
 

if __name__ == "__main__":
    main()
