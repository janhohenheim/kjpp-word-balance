from typing import Dict, List


def on_save_file(_sender, app_data: Dict[str, str], list_of_words: List[List[str]]):
    path = app_data["file_path_name"]
    separator = ";"
    with open(path, "w") as f:
        headers = [f"Kategorie {i + 1}" for i in range(len(list_of_words[0]))]
        f.write(separator.join(headers) + "\n")
        for words in list_of_words:
            f.write(separator.join(words) + "\n")
