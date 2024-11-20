import os
import sys
import pytest
from pathlib import Path

# Получаем абсолютный путь к корневой директории проекта
project_root = os.path.dirname(os.path.abspath(__file__))

# Добавляем корневую директорию в sys.path
sys.path.insert(0, project_root)

@pytest.fixture
def test_data_dir(tmp_path):
    """Фикстура для создания временной директории с тестовыми данными."""
    return tmp_path / "test_data"