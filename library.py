import json
from string import punctuation, digits
from dataclasses import dataclass, asdict


class _LibraryError:
    """Класс для обработки исключений в библиотеке"""

    title_error = "В параметр title введены неверные значения"
    author_error = "В параметр author введены неверные значения"
    year_error = "В параметр year введены неверные значения"
    id_error = "Книги с введённыи id нет в библиотеке"
    status_error = "Введён неверный статус"


@dataclass
class _Book:
    """Класс для инициализации книги"""
    _title: str
    _author: str
    _year: str
    _status: str = "в наличии"


class BookLibrary:
    """Класс для создания библиотеки"""

    def __init__(self, book_id: int = 0):
        self.__Library = {
            "books": {}
        }
        self.__id = book_id
        self.__if_add = "Книга успешно добавлена"
        self.__if_delete = "Книга успешно удалена"
        self.__if_new_status = "Статус успешно обновлён"

    def add_book(self, title: str, author: str, year: str):
        """
        Функция для добавления книги в библиотеку

        Параметры:
        1. title - Название книги
        2. author - Автор книги
        3. year - Год выпуска книги
        4. status = Статус книги, принимает 2 значения (в наличии / выдана)
        """

        book = _Book(title, author, year)
        param_errors = 0  # переменная для подсчёта ошибка в параметрах

        # ошибка, если в названии книги есть знак пунктуации
        if any([char in "".join(punctuation.split("-")) for char in title]) or not title:
            print(_LibraryError.title_error)
            param_errors += 1
        # ошибка, если в имени автора книги все знаки - знаки пунктуации или цифры
        if any([char in ("".join(punctuation.split("-")) + digits) for char in author]) or not author:
            print(_LibraryError.author_error)
            param_errors += 1
        # ошибка, если в году издания книги хотя бы один знак не цифра
        if any([(not char.isdigit()) for char in year]) or not year:
            print(_LibraryError.year_error)
            param_errors += 1
        if param_errors > 0:
            return None

        self.__id += 1
        self.__Library["books"][self.__id] = asdict(book)
        print(self.__if_add)

    def delete_book(self, book_id: int):
        """
        Функция для удаления книги из библиотеки

        Параметры:
        1. book_id - id книги
        """

        try:
            del self.__Library["books"][book_id]
        except KeyError:
            print(_LibraryError.id_error)
        else:
            print(self.__if_delete)

    def get_books(self, title: str = "", author: str = "", year: str = ""):
        """
        Функция для отображения книги по id

        Параметры:
        1. title - Название книги
        2. author - Автор книги
        3. year - Год выпуска книги
        """

        required_books = {}

        for index, book_param in self.__Library["books"].items():
            if (((not title) or book_param["_title"] == title) and
                    ((not author) or book_param["_author"] == author) and
                    ((not year) or book_param["_year"] == year)):
                required_books[index] = self.__Library["books"][index]

        return json.dumps(required_books, ensure_ascii=False)

    def get_all_books(self):
        """
        Функция для отображения всех книг
        """

        return json.dumps(self.__Library["books"], ensure_ascii=False)

    def set_new_status(self, book_id: int, status: str):
        """
        Функция для изменения статуса книги по id

        Параметры:
        1. book_id - id книги
        """

        match status:
            case "выдана" | "в наличии":
                try:
                    self.__Library["books"][book_id]["_status"] = status
                    print(self.__if_new_status)
                except KeyError:
                    print(_LibraryError.id_error)
            case _:
                print(_LibraryError.status_error)
