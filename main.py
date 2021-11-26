def main():
    """
    Библиотека.
    + список книг
    + избавиться от непечатаемых символов в списке книг
    + список книг надо хранить в txt файле
    + загрузка из файла
    - вывести список книг
    - добавить\убрать книгу в список
    - сохранить в файл обработанный список
    """

    books = []

    with open('books.txt', 'r', encoding='utf-8') as f:
        books = f.readlines()

    for i, row in enumerate(books):
        books[i] = row.strip()
        print(books[i])


if __name__ == '__main__':
    main()
