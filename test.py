import library


if __name__ == "__main__":
    
    test_library = library.BookLibrary()

    test_library.add_book("Ночь в Лиссабоне", "Эрих Мария Ремарк", "1962")
    test_library.add_book("На Западном фронте без перемен", "Эрих Мария Ремарк", "1928")

    print(test_library.get_books(author="Эрих Мария Ремарк"))

    test_library.add_book("Заводной апельсин", "Энтони Бёрджесс", "1962")
    test_library.add_book("Тестовая книга", "Энтони Бёрджесс", "1962")
    test_library.add_book(title="%^", author="12-", year="qweewr--=qwe") # пытаюсь создать книгу с неправильными параметрами

    print(test_library.get_books(author="Энтони Бёрджесс", year="1962"))
    print(test_library.get_all_books())

    test_library.delete_book(4)

    print(test_library.get_all_books())

    test_library.delete_book(10) # пытаюсь удалить книгу с несуществующим id

    test_library.set_new_status(1, "qweqwe") # пытаюсь поменять статус на некорректный
    test_library.set_new_status(1, "выдана")
