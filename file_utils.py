import pickle
import os
import json


def load_lib_from_file() -> dict:
    """Функция для дисереализации файла с библиотеками"""

    if os.path.exists("Libraries.txt"):
        with open("Libraries.txt", "rb") as lib_file:
            return pickle.load(lib_file, encoding="utf-8")
    return {}


def write_to_file(lib_name: str, lib: dict) -> None:
    """Функция для записи библиотеки в файл"""

    with open(f"{lib_name}", "w") as lib_file:
        lib_file.write(json.dumps(lib[lib_name].Library, ensure_ascii=False))


def dump_lib_to_file(lib: dict) -> None:
    """Функция для сереализации библиотеки и записи в файл Libraries.txt"""

    with open("Libraries.txt", "wb") as file:
        pickle.dump(lib, file)
