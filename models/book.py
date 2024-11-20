from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Book:
    """Класс, представляющий книгу в библиотеке."""
    
    title: str
    author: str
    year: int
    status: str = "в наличии"
    id: Optional[int] = None
    
    def to_dict(self) -> dict:
        """Преобразует объект книги в словарь для сериализации."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }
    
    @staticmethod
    def from_dict(data: dict) -> 'Book':
        """Создает объект книги из словаря."""
        return Book(
            id=data["id"],
            title=data["title"],
            author=data["author"],
            year=data["year"],
            status=data["status"]
        ) 