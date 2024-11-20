import json
import os
from typing import List, Dict, Any

class FileService:
    """Сервис для работы с файловым хранилищем."""
    
    def __init__(self, file_path: str):
        self.file_path = file_path
        self._ensure_file_exists()
    
    def _ensure_file_exists(self) -> None:
        """Проверяет существование файла и создает его при необходимости."""
        if not os.path.exists(self.file_path):
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            self.save_data([])
    
    def load_data(self) -> List[Dict[str, Any]]:
        """Загружает данные из файла."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    
    def save_data(self, data: List[Dict[str, Any]]) -> None:
        """Сохраняет данные в файл."""
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2) 