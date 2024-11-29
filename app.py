from pprint import pprint
import library


if __name__ == "__main__":

    print("""Программа для создания, управления и редактирования собственной библиотеки. 
Для начала работы введите /start""")

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

            if message == "/create_lib":
                LibraryName = input("Введите имя библиотеки: ")
                Library = library.BookLibrary()
                Libraries[LibraryName] = Library

                print("Бибилиотека успешно создана")

            elif message == "/add_book":
                LibraryName = input("""Введите имя библиотеки, в которую вы хотите добавить книгу: """)
                try:
                    Libraries[LibraryName]
                except KeyError:
                    print("Ошибка: бибилиотеки с таким именем не существует")
                else:
                    title = input("Введите название книги: ")
                    author = input("Введите автора книги: ")
                    year = int(input("Введите год написания книги: ").strip())
                    Libraries[LibraryName].add_book(title=title, author=author, year=year)

            elif message == "/get_all_books":
                LibraryName = input("""Введите имя библиотеки: """)
                try:
                    pprint(Libraries[LibraryName].get_all_books())
                except KeyError:
                    print("Ошибка: бибилиотеки с таким именем не существует")

            elif message == "/get_books":
                LibraryName = input("""Введите имя библиотеки: """)
                try:
                    Libraries[LibraryName]
                except KeyError:
                    print("Ошибка: бибилиотеки с таким именем не существует")
                else:
                    title = input("Введите название книги: ")
                    author = input("Введите автора книги: ")
                    try:
                        year = int(input("Введите год написания книги: "))
                    except ValueError:
                        year = ""
                    pprint(Libraries[LibraryName].get_books(title=title, author=author, year=year))

            elif message == "/delete_book":
                LibraryName = input("""Введите имя библиотеки: """)
                try:
                    Libraries[LibraryName]
                except KeyError:
                    print("Ошибка: бибилиотеки с таким именем не существует")
                else:
                    book_id = int(input("Введите id книги: "))

                    Libraries[LibraryName].delete_book(book_id=book_id)

            elif message == "/set_new_status":
                LibraryName = input("""Введите имя библиотеки: """)
                try:
                    Libraries[LibraryName]
                except KeyError:
                    print("Ошибка: бибилиотеки с таким именем не существует")
                else:
                    book_id = int(input("Введите id книги: "))
                    new_status = input("Введите новый статус книги: ")

                    Libraries[LibraryName].set_new_status(book_id=book_id, status=new_status)

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
