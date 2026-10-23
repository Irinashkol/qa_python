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

    @pytest.mark.parametrize('name, genre, expected_genre', [('Властелин колец', 'Фантастика', 'Фантастика'), ('Звонок', 'Ужасы', 'Ужасы'), ('Чисто английское убийство', 'Детективы','Детективы'), ('Спящая красавица', 'Мультфильмы', 'Мультфильмы'), ('Дневник Юриджит Джонс', 'Комедии', 'Комедии'), ('Зеркальный лабиринт', 'Фэнтези', ''),])

    def test_set_book_genre_success(collector, name, genre, excected_genre):
        collector.add_new_book(name) 
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == excected_genre