from pprint import pprint
import library
import file_utils


if __name__ == "__main__":

    print("""Программа для создания, управления и редактирования собственной библиотеки. 
Для начала работы введите /start""")

    try:
        start = input()

        if start == "/start":
            # булевая переменная для проверки того, выводилась ли подсказка о команде /help
            is_message_about_help = False
            # словарь для хранения библиотек

            Libraries = file_utils.load_lib_from_file()

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

                    if library_name in Libraries.keys():
                        print("Библиотека с таким именем уже существует")
                    else:
                        Libraries[library_name] = library.BookLibrary(name=library_name)
                        try:
                            file_utils.write_to_file(lib_name=library_name, lib=Libraries)
                        except OSError:
                            Libraries.pop(library_name)
                            print("Ошибка: недопустимое имя файла")
                        else:
                            if "\\" in library_name:
                                Libraries.pop(library_name)
                                print("Ошибка: недопустимое имя файла")
                            else:
                                print("Библиотека успешно создана")

                elif message == "/set_lib":
                    library_name = input("Введите имя библиотеки: ")
                    Libraries[library_name] = library.BookLibrary(name=library_name)

                    try:
                        file_utils.write_to_file(lib_name=library_name, lib=Libraries)
                    except OSError:
                        Libraries.pop(library_name)
                        print("Ошибка: недопустимое имя файла")
                    else:
                        if "\\" in library_name:
                            Libraries.pop(library_name)
                            print("Ошибка: недопустимое имя файла")
                        else:
                            print("Библиотека успешно создана")

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
                        file_utils.write_to_file(lib_name=library_name, lib=Libraries)

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

                            file_utils.write_to_file(lib_name=library_name, lib=Libraries)

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

                            file_utils.write_to_file(lib_name=library_name, lib=Libraries)

                elif message == "/get_libs":
                    pprint(Libraries)

                elif message == "/end":
                    file_utils.dump_lib_to_file(lib=Libraries)
                    print("Программа завершена")
                    break

                elif message == "":
                    continue

                else:
                    print("Ошибка: неизвестная команда")

        else:
            print("Ошибка: неизвестная команда")
    except KeyboardInterrupt:
        print("Программа завершена")

