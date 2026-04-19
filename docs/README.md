# ⚡ UI: Web Automation

> **Way2Automation** > Проект на Python для комплексного тестирования банковских и корпоративных веб-интерфейсов.

---

### 🛠 Tech Radar
* **Core:** `Python 3.10+` & `Selenium WebDriver`
* **Runner:** `Pytest` (с поддержкой параллелизации через `xdist`)
* **Reports:** `Allure Framework` (скриншоты, шаги, логи)
* **Settings:** `Pydantic` (строгая валидация окружения через `.env`)

---

### 🎯 Ключевые архитектурные решения

| Фича | Реализация | Профит |
| :--- | :--- | :--- |
| **Smart Polling** | Кастомный `wait_to_change` | Устранение «flaky» тестов на асинхронных UI |
| **Fail-Safe** | Pytest-хуки на скриншоты | Мгновенная диагностика причин падения в отчете |
| **Page Factory** | Ленивая инициализация | Оптимизация памяти при работе с тяжелыми DOM |
| **Auto-Cleanup** | Фикстуры с логикой `yield` | Всегда чистая БД после завершения сценариев |

---

### 📂 Организация кода
```bash
├── base/        # Обертки над Selenium (уровень абстракции)
├── config/      # Настройки среды и глобальные переменные
├── pages/       # Объектные модели страниц (Page Objects)
├── tests/       # Сценарии: Smoke, Regression, Transactions
└── utils/       # Инструментарий: скриншоты, логгеры, вейтеры
```
### 🚀 Быстрый старт

#### 1. Инсталляция

~~~Bash

python -m venv .venv && source .venv/bin/activate

pip install -r requirements.txt
~~~

#### 2. Конфиг (.env)
```bash
BASE_URL="[https://www.way2automation.com](https://www.way2automation.com)"

HEADLESS=true

DEFAULT_TIMEOUT=15
```

#### 3. Исполнение

~~~Bash
pytest tests/ -n 3 --alluredir=reports
~~~
📈 Результаты тестирования

Фреймворк формирует детализированный дашборд. Чтобы открыть его, используй:
~~~Bash
allure serve reports
~~~