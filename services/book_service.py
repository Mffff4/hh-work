from typing import List, Optional
from models.book import Book
from services.file_service import FileService

class BookService:
    """Сервис для управления книгами."""
    
    def __init__(self, file_service: FileService):
        self.file_service = file_service
        
    def get_all_books(self) -> List[Book]:
        """Получает список всех книг."""
        data = self.file_service.load_data()
        return [Book.from_dict(book_data) for book_data in data]
    
    def add_book(self, book: Book) -> Book:
        """Добавляет новую книгу."""
        books = self.get_all_books()
        book.id = self._generate_id(books)
        books.append(book)
        self._save_books(books)
        return book
    
    def delete_book(self, book_id: int) -> bool:
        """Удаляет книгу по ID."""
        books = self.get_all_books()
        initial_length = len(books)
        books = [book for book in books if book.id != book_id]
        if len(books) == initial_length:
            return False
        self._save_books(books)
        return True
    
    def update_status(self, book_id: int, new_status: str) -> bool:
        """Обновляет статус книги."""
        books = self.get_all_books()
        for book in books:
            if book.id == book_id:
                book.status = new_status
                self._save_books(books)
                return True
        return False
    
    def search_books(self, query: str) -> List[Book]:
        """Поиск книг по названию, автору или году."""
        books = self.get_all_books()
        query = query.lower()
        return [
            book for book in books
            if query in book.title.lower() or
               query in book.author.lower() or
               query in str(book.year)
        ]
    
    def _generate_id(self, books: List[Book]) -> int:
        """Генерирует уникальный ID для новой книги."""
        if not books:
            return 1
        return max(book.id for book in books) + 1
    
    def _save_books(self, books: List[Book]) -> None:
        """Сохраняет список книг в хранилище."""
        self.file_service.save_data([book.to_dict() for book in books]) 