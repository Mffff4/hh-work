from services.file_service import FileService
from services.book_service import BookService
from ui.menu import Menu

def main():
    """Главная функция приложения."""
    file_service = FileService("data/books.json")
    book_service = BookService(file_service)
    menu = Menu(book_service)
    menu.run()

if __name__ == "__main__":
    main()
