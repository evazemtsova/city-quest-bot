# 1. Папка → назначение

| Папка            | Назначение                                         |
|------------------|----------------------------------------------------|
| /                | Корень проекта, конфиги, pyproject.toml, README    |
| /src             | Исходный код бота                                  |
| /src/commands    | Хендлеры команд Telegram                           |
| /src/services    | Работа с CSV-файлами на GitHub, логика квеста      |
| /src/utils       | Вспомогательные функции, утилиты                   |
| /src/middleware  | Мидлвары python-telegram-bot                       |
| /src/config      | Конфиги (токены, параметры, секреты)               |
| /tests           | Тесты                                              |
| /data            | Локальные копии routes.csv и progress.csv           |

# 2. Главные файлы

- pyproject.toml или requirements.txt — зависимости проекта
- .env — переменные окружения (токены, ключи)
- /src/bot.py — входная точка Telegram-бота
- /src/services/routes.py — загрузка и парсинг routes.csv из GitHub
- /src/services/progress.py — работа с файлом progress.csv (чтение/запись через GitHub API)
- /src/services/quest.py — бизнес-логика выдачи и проверки заданий
- /src/commands/start.py — обработка /start

# 3. Генерируй новые файлы здесь

- /src/
- /src/commands/
- /src/services/
- /src/utils/
- /src/middleware/
- /src/config/
- /tests/
- /data/
