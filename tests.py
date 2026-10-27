import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector() 
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('name, genre, expected_genre', [('Властелин колец', 'Фантастика', 'Фантастика'), ('Звонок', 'Ужасы', 'Ужасы'), ('Чисто английское убийство', 'Детективы','Детективы'), ('Спящая красавица', 'Мультфильмы', 'Мультфильмы'), ('Дневник Бриджит Джонс', 'Комедии', 'Комедии'), ('Зеркальный лабиринт', 'Фэнтези', '')])

    def test_set_book_genre_success(self, collector, name, genre, expected_genre): # проверяем метод set_book_genre, возможно ли установить жанр для книги
        collector.add_new_book(name) # добавляем книгу в словарь
        collector.set_book_genre(name, genre) # устанавливаем жанр

        assert collector.get_book_genre(name) == expected_genre # сравниваем фактический жанр книги с ожидаемым.

    @pytest.mark.parametrize('name, genre, expected_genre', [('Властелин колец', 'Фантастика', 'Фантастика'), ('Звонок', 'Ужасы', 'Ужасы'), ('Нет книги', 'Фантастика', None)])

    def test_get_book_genre(self, collector, name, genre, expected_genre): # проверяем метод get_book_genre, можем ли получить жанр книги по её имени
        if name != 'Нет книги': # выполняется условие, что книга точно существует 
            collector.add_new_book(name) # добавляем книгу в словарь
            collector.set_book_genre(name, genre) # устанавливает книге жанр 

        assert collector.get_book_genre(name) == expected_genre
    @pytest.mark.parametrize('genre, expected_books', [('Фантастика', ['Властелин колец']), ('Ужасы', ['Звонок']), ('Детективы', ['Чисто английское убийство']), ('Мультфильмы', ['Спящая красавица']), ('Комедии', ['Дневник Бриджит Джонс']), ('Фэнтези',[])])
    def test_get_books_with_specific_genre(self, collector, genre, expected_books): # проверяем метод get_books_with_specific_genre, возвращает ли он список книг с указанным жанром.
        books = {
            'Властелин колец': 'Фантастика',
            'Звонок': 'Ужасы',
            'Чисто английское убийство': 'Детективы',
            'Спящая красавица': 'Мультфильмы',
            'Дневник Бриджит Джонс': 'Комедии',
        } # создаем словарь с названиями и жанрами
        for name, book_genre in books.items(): #  добавляем каждое название в коллекцию и устанавливаем жанр
            collector.add_new_book(name)
            collector.set_book_genre(name, book_genre)
        assert collector.get_books_with_specific_genre(genre) == expected_books # запрашиваем книги по переданному жанру и сравниваем результат со списком
    def test_get_books_genre(self, collector): # проверяем метод get_books_genre, возвращает ли он словарь
        collector.add_new_book('Властелин колец') # добавляем книгу в коллекцию
        collector.set_book_genre('Властелин колец', 'Фантастика') # Присваиваем жанр
        assert collector.get_books_genre() == {'Властелин колец': 'Фантастика'} # проверяем, что метод вернул словарь 
    @pytest.mark.parametrize('name, genre, is_for_children', [('Властелин колец', 'Фантастика', True), ('Звонок', 'Ужасы', False), ('Чисто английское убийство', 'Детективы', False), ('Спящая красавица', 'Мультфильмы', True), ('Дневник Юриджит Джонс', 'Комедии', True)])  
    def test_get_books_for_children(self, collector, name, genre, is_for_children): # проверяем, метод get_books_for_children
        collector.add_new_book(name) # добавляем книгу
        collector.set_book_genre(name, genre) # устанавливаем жанр
        result = collector.get_books_for_children() # получаем список книг для детей
        assert (name in result) is is_for_children # проверяем, что результат соответвует возрастному рейтингу
    def test_add_book_in_favorites(self, collector): # проверяем метод, что он добавляет в список Избранное
        collector.add_new_book('Властелин колец')

        collector.add_book_in_favorites('Властелин колец')
        assert collector.get_list_of_favorites_books() == ['Властелин колец'] # проверяем, что добавленная книга добавилась в список Избранного
    def test_delete_book_from_favorites(self, collector): # проверяем, что метод delete_book_from_favorites удаляет книгу из списка Избранного
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец') 
        collector.delete_book_from_favorites('Властелин колец')
        assert collector.get_list_of_favorites_books() == []
    def test_get_list_of_favorites_books(self, collector): # Проверяем метод get_list_of_favorites_books, что возможно получить список Избранного
        collector.add_new_book('Властелин колец') # добавляем книгу
        collector.add_book_in_favorites('Властелин колец') # добавляем книгу в избранное
        assert collector.get_list_of_favorites_books() == ['Властелин колец'] # проеряем, что метод вернул список с добаленной книгой
    def test_get_list_of_favorites_books_returns_empty_list(self, collector): # Проверяем метод get_list_of_favorites_books, что при пустом списке Избранного метод выдаст пустой список.
        assert collector.get_list_of_favorites_books() == []