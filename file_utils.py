import pickle
import os
import json


LIBRARY_DIR = "libraries"
os.makedirs(LIBRARY_DIR, exist_ok=True)


def load_lib_from_file() -> dict:
    """Функция для дисереализации файла с библиотеками"""

    if os.path.exists("Libraries.txt"):
        with open("Libraries.txt", "rb") as lib_file:
            return pickle.load(lib_file, encoding="utf-8")
    return {}


def write_to_file(lib_name: str, lib: dict) -> None:
    """Функция для записи библиотеки в файл"""

    file_path = os.path.join(LIBRARY_DIR, f"{lib_name}")
    with open(file_path, "w", encoding="utf-8") as lib_file:
        lib_file.write(json.dumps(lib[lib_name].Library, ensure_ascii=False))


def dump_lib_to_file(lib: dict) -> None:
    """Функция для сереализации библиотеки и записи в файл Libraries.txt"""

    with open("Libraries.txt", "wb") as file:
        pickle.dump(lib, file)
