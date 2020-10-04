# Лабораторная работа  №1

### Задание
Написать программу на Python, которая:

* Подсчитывает общее количество символов в файле
* Подсчитывает общее количесто символов без пробелов
* Подсчитывает количество символов без знаков препинания
* Подсчитывает количество слов в файле
* Подсчитывает количество предложений
* Результат подсчета должен быть выведен в консоль

**Вход программы:**
Файл `steam_description_data.csv`

**Выход программы:**
Информация о количестве символов, слов и предложений

> **_ВАЖНО:_**
Результат оформить в виде репозитория на гитхабе.

### Решение 1
* Use the Tkinter GUI, create a window and then select the csv file to use to study. Read csv file.
* The list of records obtained when reading the file is again glued into one line
* String length as determined by the len () function
* The count function returns the number of occurrences of the desired object (spaces, punctuation ...)
* Using the re module, a search for words and sentences is performed:
*Words are found using the pattern: `(\ w + '\ w +) | (\ w + - \ w +' \ w +) | (\ w + - \ w + '\ w) | \ w +`
*Sentences are defined using the pattern: `([A-Z] [^ \.!?] * [\.!?])`
