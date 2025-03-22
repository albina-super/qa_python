from data_for_tests import TITLE_MORE_41_SYMBOL, EMPTY_TITLE, VALIDE_BOOK, VALIDE_GENRE
from main import BooksCollector
import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2


    @pytest.mark.parametrize('title',[
        EMPTY_TITLE,
        TITLE_MORE_41_SYMBOL
    ])
    def test_add_new_book_validate_length_title(self, title):
        collector = BooksCollector()
        collector.add_new_book(title)

        list_books = collector.get_books_genre()

        assert title not in list_books


    def test_set_book_genre_success(self, collector_book_without_genre):
        collector_book_without_genre.set_book_genre(VALIDE_BOOK, VALIDE_GENRE)
        list_books = collector_book_without_genre.get_books_genre()
        assert VALIDE_BOOK in list_books
        assert list_books[VALIDE_BOOK] == VALIDE_GENRE


    def test_get_book_genre_success(self, collector_book_without_genre):
        assert collector_book_without_genre.get_book_genre(VALIDE_BOOK) == VALIDE_GENRE

    def test_get_books_with_specific_genre_success(self, collector_book_with_genre):
        books_list = collector_book_with_genre.get_books_with_specific_genre(VALIDE_GENRE)
        assert VALIDE_BOOK in books_list

    def test_get_books_genre(self, collector_book_with_genre):
        assert collector_book_with_genre.get_books_genre() == collector_book_with_genre.books_genre

    def test_get_books_for_children_success(self, collector_book_with_genre):
        children_books = collector_book_with_genre.get_books_for_children()
        assert VALIDE_BOOK in children_books


    def test_add_book_in_favorites_success(self, collector_book_with_genre):
        collector_book_with_genre.favorites.append(VALIDE_BOOK)
        assert VALIDE_BOOK in collector_book_with_genre.favorites


    def test_delete_book_from_favorites_success(self, collector_with_favorites):
        collector_with_favorites.delete_book_from_favorites(VALIDE_BOOK)
        assert VALIDE_BOOK not in collector_with_favorites.favorites


    def test_get_list_of_favorites_books_success(self, collector_with_favorites):
        assert type(collector_with_favorites.get_list_of_favorites_books()) == list
        assert len(collector_with_favorites.get_list_of_favorites_books()) != 0