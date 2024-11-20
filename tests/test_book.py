import pytest
from models.book import Book

def test_book_creation():
    """Тест создания книги."""
    book = Book(title="Война и мир", author="Л.Н. Толстой", year=1869)
    assert book.title == "Война и мир"
    assert book.author == "Л.Н. Толстой"
    assert book.year == 1869
    assert book.status == "в наличии"
    assert book.id is None

def test_book_to_dict():
    """Тест преобразования книги в словарь."""
    book = Book(title="Война и мир", author="Л.Н. Толстой", year=1869, id=1)
    book_dict = book.to_dict()
    
    assert book_dict["id"] == 1
    assert book_dict["title"] == "Война и мир"
    assert book_dict["author"] == "Л.Н. Толстой"
    assert book_dict["year"] == 1869
    assert book_dict["status"] == "в наличии"

def test_book_from_dict():
    """Тест создания книги из словаря."""
    book_dict = {
        "id": 1,
        "title": "Война и мир",
        "author": "Л.Н. Толстой",
        "year": 1869,
        "status": "выдана"
    }
    
    book = Book.from_dict(book_dict)
    assert book.id == 1
    assert book.title == "Война и мир"
    assert book.author == "Л.Н. Толстой"
    assert book.year == 1869
    assert book.status == "выдана" 