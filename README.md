# MongoDB + FASTApi

## Развертывание

1. Склонировать проект ```git clone https://github.com/777boeing777/mongo-forms.git```
2. Создать .env и скопировать туда переменные из .env.example (.env должен находиться на том же уровне, что и .env.example)
3. Поднять проект ```docker-compose up --build```


## Тестирование
Для удобного тестирования необходимо установить зависимости проекта
1. Войти в виртуальное окружение poetry ```poetry shell```
2. Установить зависимости ```poetry install```
3. Чтобы иметь возможность запускать скрипт из среды разработки, можно найти путь интерпретатора, для этого можно выполнить ```which python``` (внутри окружения)

В src/ находится файл script.py. В нем подготовлены данные и функции для тестирования приложения.
1. add_forms - загрузить в БД тестовые шаблоны форм
2. get_form - проверка сервиса с корректными формами
3. get_form_not_in_database - проверка сервиса с формами, которых нет БД

URL свагера - http://127.0.0.1:8000/api/docs
