import json
from dataclasses import dataclass, asdict
from typing import Optional


class LibraryError(Exception):
    """Класс для обработки исключений в библиотеке"""

    title_error = ValueError("В параметр title введены неверные значения")
    author_error = ValueError("В параметр author введены неверные значения")
    year_error = ValueError("В параметр year введены неверные значения")
    id_error = "Книги с введённыи id нет в библиотеке"
    status_error = ValueError("Введён неверный статус")


@dataclass
class _Book:
    """Класс для инициализации книги"""
    _title: str
    _author: str
    _year: int
    _status: str = "в наличии"


class BookLibrary:
    """Класс для создания библиотеки"""

    def __init__(self, book_id: int = 0):
        self.__Library = {
            "books": {}
        }
        self.__id = book_id

    def add_book(self, title: str, author: str, year: int):
        """
        Функция для добавления книги в библиотеку

        Параметры:
        1. title - Название книги
        2. author - Автор книги
        3. year - Год выпуска книги
        4. status = Статус книги, принимает 2 значения (в наличии / выдана)
        """

        self.__id += 1
        book = _Book(title, author, year)

        if not isinstance(title, str):
            raise LibraryError.title_error
        elif not isinstance(author, str):
            raise LibraryError.author_error
        elif not isinstance(year, int):
            raise LibraryError.year_error
        else:
            self.__Library["books"][self.__id] = asdict(book)

    def delete_book(self, book_id: int):
        """
        Функция для удаления книги из библиотеки

        Параметры:
        1. book_id - id книги
        """

        try:
            del self.__Library["books"][book_id]
        except KeyError:
            print(LibraryError.id_error)

    def get_books(self, title: Optional[str] = None, author: Optional[str] = None, year: Optional[int] = None):
        """
        Функция для отображения книги по id

        Параметры:
        1. title - Название книги
        2. author - Автор книги
        3. year - Год выпуска книги
        """

        required_books = {}

        for index, book_param in self.__Library["books"].items():
            if ((title is None or book_param["title"] == title) and
                    (author is None or book_param["author"] == author) and
                    (year is None or book_param["year"] == year)):
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
                    self.__Library["books"][book_id]["status"] = status
                except KeyError:
                    print(LibraryError.id_error)
            case _:
                raise LibraryError.status_error
        
