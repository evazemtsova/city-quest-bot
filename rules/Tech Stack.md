# Tech Stack for Telegram City Quest Bot

| Layer            | Library / Service            | Version            | Purpose                                                        | Docs Link                                                                             |
|------------------|-----------------------------|--------------------|----------------------------------------------------------------|---------------------------------------------------------------------------------------|
| Runtime          | Python                      | 3.12               | Python runtime environment                                      | [Python Docs](https://docs.python.org/3/)                                             |
| Bot SDK          | python-telegram-bot         | 21.x               | Telegram Bot API for Python                                     | [python-telegram-bot Docs](https://docs.python-telegram-bot.org/)                     |
| Data Storage     | GitHub (CSV files)          | n/a                | Хранение маршрутов (routes.csv) и прогресса (progress.csv)      | [GitHub Docs](https://docs.github.com/en/rest)                                        |
| GitHub API       | PyGithub                    | 2.x                | Для автоматической загрузки и обновления CSV-файлов в GitHub    | [PyGithub Docs](https://pygithub.readthedocs.io/en/stable/introduction.html)          |
| Deployment       | Railway                     | n/a                | Хостинг и деплой Python приложений                              | [Railway Docs](https://railway.app/docs)                                              |
| Линтер/Форматтер | ruff + black                | ruff 0.x / black 24.x | Анализ кода и автоформатирование                             | [Ruff Docs](https://docs.astral.sh/ruff/) / [Black Docs](https://black.readthedocs.io/en/stable/) |
