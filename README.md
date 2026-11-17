# ЛР9. Запуск модульных тестов в GitHub Actions

При каждом push GitHub запускает тесты калькулятора на Ubuntu с Python 3.14. Тесты проверяют сложение, деление, обработку нулевого делителя и определение простых чисел.

## Запуск на компьютере

Из корня проекта выполните:

    python -m pip install -r requirements.txt
    python -m pytest -v

## Проверка в GitHub

После загрузки файлов откройте Actions → Calculator tests → последний запуск → test → Run unit tests. Ожидаемый результат — 18 passed.
