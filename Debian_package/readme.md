# Небольшие подсказски про сборку дебиановских пакетов

В сборке дебиановского пакета нам важны файлы: (их значение вы можете поискать дальше, мне пока лень это писать)
- debian/control
- debian/rules
- debian/changelog
- debian/install

1. Пример пакета есть тут https://github.com/bob4inski/sirius-tasks/tree/main/cats
2. Синтаксис debian пакетов https://www.debian.org/doc/debian-policy/ch-controlfields.html
2. https://blog.packagecloud.io/buildling-debian-packages-with-debuild/
3. https://john-tucker.medium.com/debian-packaging-by-example-118c18f5dbfe


## Задание
1. Собрать пакетик с приложением на python3 которое позволит запускать приложеньку через systemd
    1. Обернуть питончик в пакет
    2. Прописать зависимости
    3. Прописать запуск приложения через systemd
    4. Установить пакет
