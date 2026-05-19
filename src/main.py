#!/usr/bin/env python3
"""
Скрипт для ротации ключей opencode-go
"""

import sys
import os

# Добавляем корневую директорию в path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.config import config


def main():
    """Главная функция"""
    try:
        config.validate()
        print(f"Загружено {len(config.opencode_keys)} ключей")
        print(f"Файлы настроек: {config.config_files}")
        print("Скрипт готов к работе")
    except ValueError as e:
        print(f"Ошибка конфигурации: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Неожиданная ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
