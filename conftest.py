import pytest
from data_for_tests import VALIDE_BOOK, VALIDE_GENRE

from main import BooksCollector

@pytest.fixture(scope='session')
def collector_book_without_genre():
    # print('adding book')
    collector = BooksCollector()
    collector.add_new_book(VALIDE_BOOK)
    return collector


@pytest.fixture(scope='session')
def collector_book_with_genre():
    collector = BooksCollector()
    collector.add_new_book(VALIDE_BOOK)
    collector.set_book_genre(VALIDE_BOOK, VALIDE_GENRE)
    return collector

@pytest.fixture
def collector_with_favorites():
    collector = BooksCollector()
    collector.add_new_book(VALIDE_BOOK)
    collector.set_book_genre(VALIDE_BOOK, VALIDE_GENRE)
    collector.add_book_in_favorites(VALIDE_BOOK)
    return collector