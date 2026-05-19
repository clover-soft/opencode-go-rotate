# Этап 1: Начальная настройка

## Задачи

- [x] Инициализация Python проекта
- [x] Создание структуры директорий
- [x] Настройка зависимостей
- [x] Создание базового конфигурационного файла

## Детали

### Структура проекта

```
opencode-go-rotate/
├── src/
│   ├── main.py
│   ├── config.py
│   └── utils.py
├── tests/
│   └── test_basic.py
├── data/
│   └── stats.json
├── config.yaml
├── requirements.txt
└── .env.example
```

### Зависимости

- `pyyaml` - для работы с конфигурациями
- `python-dotenv` - для работы с .env файлами
- `requests` - для API запросов (если нужно)

### Конфигурация

Файл `.env` должен содержать ключи opencode-go:
```
OPENCODE_GO_KEY_001=key1
OPENCODE_GO_KEY_002=key2
OPENCODE_GO_KEY_003=key3
```

Файл `config.yaml` должен содержать:
- Пути к файлам настроек
- Имена ключей в каждом файле
- Параметры сбора статистики
