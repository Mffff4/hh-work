import os
from typing import List
import questionary
from models.book import Book
from services.book_service import BookService

class Menu:
    """Класс для управления пользовательским интерфейсом."""
    
    def __init__(self, book_service: BookService):
        self.book_service = book_service
        self.options = {
            "Показать все книги": self.show_all_books,
            "Добавить книгу": self.add_book,
            "Удалить книгу": self.delete_book,
            "Поиск книги": self.search_books,
            "Изменить статус книги": self.change_status,
            "Выход": exit
        }
    
    def clear_screen(self):
        """Очищает экран консоли."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def run(self):
        """Запускает главное меню."""
        while True:
            self.clear_screen()
            print("\n=== Система управления библиотекой ===\n")
            
            action = questionary.select(
                "Выберите действие:",
                choices=list(self.options.keys())
            ).ask()
            
            self.clear_screen()
            self.options[action]()
    
    def show_all_books(self):
        """Отображает все книги."""
        books = self.book_service.get_all_books()
        self._display_books(books)
        input("\nНажмите Enter для продолжения...")
    
    def add_book(self):
        """Добавляет новую книгу."""
        print("\n=== Добавление новой книги ===\n")
        try:
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания: "))
            
            book = Book(title=title, author=author, year=year)
            self.book_service.add_book(book)
            print("\nКнига успешно добавлена!")
        except ValueError:
            print("\nОшибка: Год должен быть числом!")
        input("\nНажмите Enter для продолжения...")
    
    def delete_book(self):
        """Удаляет книгу."""
        print("\n=== Удаление книги ===\n")
        try:
            book_id = int(input("Введите ID книги для удаления: "))
            if self.book_service.delete_book(book_id):
                print("\nКнига успешно удалена!")
            else:
                print("\nКнига с указанным ID не найдена!")
        except ValueError:
            print("\nОшибка: ID должен быть числом!")
        input("\nНажмите Enter для продолжения...")
    
    def search_books(self):
        """Поиск книг."""
        print("\n=== Поиск книг ===\n")
        query = input("Введите поисковый запрос: ")
        books = self.book_service.search_books(query)
        if books:
            self._display_books(books)
        else:
            print("\nКниги не найдены!")
        input("\nНажмите Enter для продолжения...")
    
    def change_status(self):
        """Изменяет статус книги."""
        print("\n=== Изменение статуса книги ===\n")
        try:
            book_id = int(input("Введите ID книги: "))
            status = input("Введите новый статус (в наличии/выдана): ")
            if status not in ["в наличии", "выдана"]:
                print("\nОшибка: Неверный статус!")
                return
            
            if self.book_service.update_status(book_id, status):
                print("\nСтатус книги успешно обновлен!")
            else:
                print("\nКнига с указанным ID не найдена!")
        except ValueError:
            print("\nОшибка: ID должен быть числом!")
        input("\nНажмите Enter для продолжения...")
    
    def _display_books(self, books: List[Book]):
        """Отображает список книг в табличном формате."""
        if not books:
            print("\nБиблиотека пуста!")
            return
        
        print("\nСписок книг:")
        print("-" * 80)
        print(f"{'ID':^5} | {'Название':^25} | {'Автор':^20} | {'Год':^6} | {'Статус':^10}")
        print("-" * 80)
        
        for book in books:
            print(f"{book.id:^5} | {book.title[:25]:25} | {book.author[:20]:20} | "
                  f"{book.year:^6} | {book.status:^10}") 