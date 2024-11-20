import pytest
import os
from services.file_service import FileService
from services.book_service import BookService
from models.book import Book

@pytest.fixture
def test_file_path(tmp_path):
    """Фикстура для создания временного файла."""
    return str(tmp_path / "test_books.json")

@pytest.fixture
def book_service(test_file_path):
    """Фикстура для создания сервиса книг."""
    file_service = FileService(test_file_path)
    return BookService(file_service)

def test_add_book(book_service):
    """Тест добавления книги."""
    book = Book(title="Тест", author="Автор", year=2024)
    added_book = book_service.add_book(book)
    
    assert added_book.id is not None
    assert added_book.title == "Тест"
    
    books = book_service.get_all_books()
    assert len(books) == 1
    assert books[0].id == added_book.id

def test_delete_book(book_service):
    """Тест удаления книги."""
    book = Book(title="Тест", author="Автор", year=2024)
    added_book = book_service.add_book(book)
    
    assert book_service.delete_book(added_book.id) is True
    assert len(book_service.get_all_books()) == 0

def test_search_books(book_service):
    """Тест поиска книг."""
    book1 = Book(title="Первая книга", author="Автор", year=2024)
    book2 = Book(title="Вторая книга", author="Другой автор", year=2023)
    
    book_service.add_book(book1)
    book_service.add_book(book2)
    
    results = book_service.search_books("Первая")
    assert len(results) == 1
    assert results[0].title == "Первая книга"
    
    results = book_service.search_books("автор")
    assert len(results) == 2

def test_update_status(book_service):
    """Тест обновления статуса книги."""
    book = Book(title="Тест", author="Автор", year=2024)
    added_book = book_service.add_book(book)
    
    assert book_service.update_status(added_book.id, "выдана") is True
    
    updated_books = book_service.get_all_books()
    assert updated_books[0].status == "выдана" 