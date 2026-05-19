import os
from dotenv import load_dotenv
from typing import List

load_dotenv()


class Config:
    """Конфигурация проекта"""

    def __init__(self):
        self.opencode_keys: List[str] = self._parse_keys()
        self.config_files: List[str] = self._parse_config_files()
        self.stats_update_interval: int = int(os.getenv("STATS_UPDATE_INTERVAL", "3600"))
        self.stats_file: str = os.getenv("STATS_FILE", "./data/stats.json")
        self.debug: bool = os.getenv("DEBUG", "false").lower() == "true"

    def _parse_keys(self) -> List[str]:
        keys_str = os.getenv("OPENCODE_KEYS", "")
        return [key.strip() for key in keys_str.split(",") if key.strip()]

    def _parse_config_files(self) -> List[str]:
        files_str = os.getenv("CONFIG_FILES", "")
        return [file.strip() for file in files_str.split(",") if file.strip()]

    def validate(self) -> bool:
        """Проверка валидности конфигурации"""
        if not self.opencode_keys:
            raise ValueError("OPENCODE_KEYS не задан")
        if not self.config_files:
            raise ValueError("CONFIG_FILES не задан")
        return True


config = Config()
