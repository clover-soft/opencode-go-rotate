# opencode-go-rotate

Скрипт для ротации ключей opencode-go в файлах настроек. Определяет наименее использованный ключ и прописывает его в конфигурационных файлах, чтобы ассистенты использовали ключ с наибольшими ресурсами.

## Назначение

Скрипт анализирует статистику использования ключей opencode-go и автоматически выбирает ключ с наименьшей нагрузкой для записи в конфигурационные файлы. Это обеспечивает равномерное распределение нагрузки между ключами и предотвращает исчерпание лимитов.

## Документация

- [Контекст проекта](docs/context.md) - описание контекста и целей проекта
- [Этапы разработки](docs/steps/) - пошаговый план разработки

## Структура проекта

```
opencode-go-rotate/
├── README.md
├── config.yaml
├── .env.example
├── requirements.txt
├── docs/
│   ├── context.md
│   └── steps/
│       ├── 01-initial-setup.md
│       ├── 02-key-statistics.md
│       ├── 03-rotation-logic.md
│       └── 04-integration.md
├── src/
│   ├── main.py
│   ├── config.py
│   └── utils.py
├── tests/
│   └── test_basic.py
└── data/
    └── stats.json
```

## Конфигурация

### Ключи opencode-go

Ключи задаются в `.env` файле:
```bash
OPENCODE_GO_API_KEY_001=key1
OPENCODE_GO_API_KEY_002=key2
OPENCODE_GO_API_KEY_003=key3
```

### Файлы для обновления

Список файлов задается в `config.yaml`:
```yaml
config_files:
  - "/path/to/.env1"
  - "/path/to/config.yaml"
```

## Использование

```bash
# Установка зависимостей
pip3 install -r requirements.txt

# Настройка конфигурации
cp .env.example .env
# отредактировать .env и config.yaml

# Запуск ротации ключей
python3 src/main.py
```

## Требования

- Python 3.14+
- Доступ к файлам настроек opencode-go
