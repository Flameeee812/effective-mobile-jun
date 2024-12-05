import json
from pprint import pprint
import library

if __name__ == "__main__":

    print("""Программа для создания, управления и редактирования собственной библиотеки. 
Для начала работы введите /start""")


    def write_to_file(lib_name: str) -> None:
        """Функция для записи библиотеки в файл"""
        with open(f"{lib_name}", "w") as lib_file:
            lib_file.write(json.dumps(my_library.Library, ensure_ascii=False))

    start = input()

    if start == "/start":
        # булевая переменная для проверки того, выводилась ли подсказка о команде /help
        is_message_about_help = False
        # словарь для хранения библиотек

        Libraries = {}

        while True:
            if not is_message_about_help:
                print("""Для того, чтобы узнать список команд - введите /help""")
            # после вывода подсказки переменная принимает значение  True и не выводит подсказку
            is_message_about_help = True

            message = input()

            if message == "/help":
                print("""  Команды:
        1. /create_lib - Команда для создания бибилиотеки
        2. /add_book - Добавляет книгу с введёнными 
        пользователем title/author/year
        3. /get_all_books - Отображает библиотеку
        4. /get_books - Отображает книги по title/author/year
        5. /delete_book - Удаляет книгу по id
        6. /set_new_status - Обновляет статус книги.
        Принимает только 2 статуса: 'в наличии'/'выдана'
        7. /get_libs - Отображает все библиотеки
        8. /end - Завершает работу приложения""")

            elif message == "/create_lib":

                library_name = input("Введите имя библиотеки: ")
                my_library = library.BookLibrary()
                Libraries[library_name] = my_library

                try:
                    write_to_file(library_name)
                    print("Бибилиотека успешно создана")
                except OSError:
                    print("Ошибка: недопустимое имя файла")

            elif message == "/add_book":
                library_name = input("""Введите имя библиотеки, в которую вы хотите добавить книгу: """)
                try:
                    Libraries[library_name]
                except KeyError:
                    print("Ошибка: бибилиотеки с таким именем не существует")
                else:
                    lib = Libraries[library_name]
                    title = input("Введите название книги: ").strip()
                    author = input("Введите автора книги: ").strip()
                    year = input("Введите год написания книги: ").strip()

                    lib.add_book(title=title, author=author, year=year)
                    write_to_file(library_name)

            elif message == "/get_all_books":
                library_name = input("""Введите имя библиотеки: """)
                try:
                    lib = Libraries[library_name]
                    pprint(lib.get_all_books())
                except KeyError:
                    print("Ошибка: бибилиотеки с таким именем не существует")

            elif message == "/get_books":
                library_name = input("""Введите имя библиотеки: """)
                try:
                    Libraries[library_name]
                except KeyError:
                    print("Ошибка: бибилиотеки с таким именем не существует")
                else:
                    lib = Libraries[library_name]
                    title = input("Введите название книги: ")
                    author = input("Введите автора книги: ")
                    year = input("Введите год написания книги: ")

                    pprint(lib.get_books(title=title, author=author, year=year))

            elif message == "/delete_book":
                library_name = input("""Введите имя библиотеки: """)
                try:
                    Libraries[library_name]
                except KeyError:
                    print("Ошибка: бибилиотеки с таким именем не существует")
                else:
                    try:
                        book_id = int(input("Введите id книги: "))
                    except ValueError:
                        print("id должно быть числом")
                    else:
                        lib = Libraries[library_name]
                        lib.delete_book(book_id=book_id)

                        write_to_file(library_name)

            elif message == "/set_new_status":
                library_name = input("""Введите имя библиотеки: """)
                try:
                    Libraries[library_name]
                except KeyError:
                    print("Ошибка: бибилиотеки с таким именем не существует")
                else:
                    try:
                        book_id = int(input("Введите id книги: "))
                    except ValueError:
                        print("id должно быть числом")
                    else:
                        lib = Libraries[library_name]
                        new_status = input("Введите новый статус книги: ")
                        lib.set_new_status(book_id=book_id, status=new_status)

                        write_to_file(library_name)

            elif message == "/get_libs":
                pprint(Libraries)

            elif message == "/end":
                break

            elif message == "":
                continue

            else:
                print("Ошибка: неизвестная команда")

    else:
        print("Ошибка: неизвестная команда")
