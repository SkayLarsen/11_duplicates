# Anti-Duplicator

Скрипт принимает на вход папку, просматривает все файлы в ней (и во всех подпапках) и сообщает, если находит дубликаты. 
Дубликаты – это два файла с одинаковым именем и размером.

Скрипт требует для своей работы установленный интерпретатор Python версии 3.5

Запуск на Linux:

```#!bash
$ python duplicates.py <path to folder>
```
Запуск на Windows происходит аналогично.

Пример вывода скрипта:

```
Дубликаты:      ./.git/logs/HEAD и ./.git/logs/refs/remotes/origin/HEAD
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
