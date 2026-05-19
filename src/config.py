import os
from dotenv import load_dotenv
from typing import List, Dict
import yaml

load_dotenv()


class Config:
    """Конфигурация проекта"""

    def __init__(self):
        self.opencode_keys: Dict[str, str] = self._parse_keys()
        self.config_files: List[str] = self._load_config_files()
        self.stats_update_interval: int = int(os.getenv("STATS_UPDATE_INTERVAL", "3600"))
        self.stats_file: str = os.getenv("STATS_FILE", "./data/stats.json")
        self.debug: bool = os.getenv("DEBUG", "false").lower() == "true"

    def _parse_keys(self) -> Dict[str, str]:
        """Парсит ключи из переменных окружения OPENCODE_GO_KEY_XXX"""
        keys = {}
        for key, value in os.environ.items():
            if key.startswith("OPENCODE_GO_KEY_"):
                keys[key] = value
        return keys

    def _load_config_files(self) -> List[str]:
        """Загружает список файлов из config.yaml"""
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.yaml")
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Файл конфигурации не найден: {config_path}")
        
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        
        return config.get('config_files', [])

    def validate(self) -> bool:
        """Проверка валидности конфигурации"""
        if not self.opencode_keys:
            raise ValueError("OPENCODE_GO_KEY_* не заданы")
        if not self.config_files:
            raise ValueError("config_files не задан в config.yaml")
        return True


config = Config()
