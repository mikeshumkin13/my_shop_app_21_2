#  My Shop App 21.2

Небольшое учебное веб-приложение, реализующее макет интернет-магазина с помощью Python и стандартной библиотеки `http.server`.

##  Технологии

- Python 3.12
- HTML + CSS (Bootstrap 5)
- Минимальный HTTP-сервер (`http.server`)
- Bootstrap подключён локально (в папке `static`)

##  Запуск проекта

1. Клонируй репозиторий:

git clone https://github.com/your-username/my_shop_app_21_2.git
cd my_shop_app_21_2

2. Активируй виртуальное окружение:
poetry install
poetry shell

3. Запусти сервер
python3 main.py

4. Открой в браузере:
http://localhost:8080


## Структура проекта
.
├── README.md
├── main.py
├── pyproject.toml
├── static
│   ├── css
│   │   └── bootstrap.min.css
│   └── js
│       └── bootstrap.bundle.min.js
└── templates
    ├── catalog.html
    ├── category.html
    ├── contacts.html
    └── index.html

5 directories, 9 files

## Возможности

 - Переключение между страницами (Главная, Каталог, Категория, Контакты)
 - Форму обратной связи на странице "Контакты"
 - Обработка POST-запроса и вывод данных формы в консоль
 - Статическая отдача CSS/JS файлов

Проект создан в рамках домашнего задания 21.2 курса Skypro
