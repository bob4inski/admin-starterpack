# Шпаргалка по командам для работы с процессами и файловой системой

## Работа с процессами

### Просмотр процессов
| Команда | Описание | Пример |
|---------|----------|--------|
| `ps aux` | Показать все процессы | `ps aux` |
| `ps -u user` | Показать процессы пользователя | `ps -u $USER` |
| `ps -ef` | Показать все процессы в другом формате | `ps -ef` |
| `top` | Интерактивный просмотр процессов | `top` |
| `atop` | |   `atop -R /var/log/atop.daily` |
| `htop` | Улучшенная версия top | `htop` |
| `pstree` | Дерево процессов | `pstree` |
| `pgrep` | Найти процессы по имени | `pgrep nginx` |
| `pidof` | Найти PID процесса по имени | `pidof nginx` |

### Управление процессами
| Команда | Описание | Пример |
|---------|----------|--------|
| `kill PID` | Отправить сигнал процессу | `kill 1234` |
| `kill -15 PID` | Отправить SIGTERM (корректное завершение) | `kill -15 1234` |
| `kill -9 PID` | Отправить SIGKILL (принудительное завершение) | `kill -9 1234` |
| `killall name` | Завершить процессы по имени | `killall nginx` |
| `pkill pattern` | Завершить процессы по шаблону | `pkill "nginx.*worker"` |
| `nice -n value command` | Запустить с приоритетом | `nice -n 10 command` |
| `renice value PID` | Изменить приоритет процесса | `renice 10 1234` |
| `nohup command &` | Выполнить после завершения сессии | `nohup script.sh &` |
| `jobs` | Показать фоновые задачи | `jobs` |
| `bg %n` | Перевести задачу в фон | `bg %1` |
| `fg %n` | Перевести задачу на передний план | `fg %1` |
| `Ctrl+Z` | Приостановить текущую задачу | - |
| `Ctrl+C` | Прервать текущую задачу | - |

## Работа с файловой системой

### Просмотр информации о файловой системе
| Команда | Описание | Пример |
|---------|----------|--------|
| `df -h` | Информация о файловых системах | `df -h` |
| `df -i` | Информация об inode | `df -i` |
| `du -sh dir` | Размер директории | `du -sh /home` |
| `du -ah` | Размер всех файлов и директорий | `du -ah` |
| `lsblk` | Блочные устройства | `lsblk` |
| `mount` | Смонтированные файловые системы | `mount` |
| `findmnt` | Смонтированные файловые системы (другой формат) | `findmnt` |
| `stat file` | Детальная информация о файле | `stat file.txt` |

### Поиск файлов
| Команда | Описание | Пример |
|---------|----------|--------|
| `find path -name pattern` | Найти файлы по имени | `find . -name "*.txt"` |
| `find path -type f` | Найти только файлы | `find . -type f` |
| `find path -type d` | Найти только директории | `find . -type d` |
| `find path -size +N` | Найти файлы размером больше N | `find . -size +1M` |
| `find path -mtime -N` | Изменённые за последние N дней | `find . -mtime -7` |
| `find path -mmin -N` | Изменённые за последние N минут | `find . -mmin -60` |
| `locate pattern` | Быстрый поиск по базе | `locate "*.conf"` |
| `which command` | Путь к исполняемому файлу | `which python` |
| `whereis command` | Расположение команды | `whereis python` |
| `type command` | Тип команды | `type ls` |

## Работа с правами доступа

### Просмотр и изменение прав
| Команда | Описание | Пример |
|---------|----------|--------|
| `ls -la` | Показать права доступа | `ls -la` |
| `ls -ld dir` | Права директории | `ls -ld /home` |
| `chmod mode file` | Изменить права доступа | `chmod 755 script.sh` |
| `chmod u+x file` | Добавить право выполнения владельцу | `chmod u+x script.sh` |
| `chmod g-w file` | Убрать право записи для группы | `chmod g-w file.txt` |
| `chmod o=r file` | Установить права только для чтения для других | `chmod o=r file.txt` |
| `chmod -R mode dir` | Рекурсивно изменить права | `chmod -R 755 /dir` |
| `chown user:group file` | Изменить владельца и группу | `chown user:group file.txt` |
| `chown user file` | Изменить только владельца | `chown user file.txt` |
| `chgrp group file` | Изменить только группу | `chgrp group file.txt` |
| `chown -R user:group dir` | Рекурсивно изменить владельца | `chown -R user:group /dir` |

### Специальные права
| Команда | Описание | Пример |
|---------|----------|--------|
| `chmod u+s file` | Установить SUID | `chmod u+s /usr/bin/passwd` |
| `chmod g+s dir` | Установить SGID | `chmod g+s /shared` |
| `chmod o+t dir` | Установить sticky bit | `chmod o+t /tmp` |
| `getfacl file` | Показать ACL | `getfacl file.txt` |
| `setfacl` | Установить ACL | `setfacl -m u:user:rwx file.txt` |

## Работа с текстом

### Просмотр содержимого
| Команда | Описание | Пример |
|---------|----------|--------|
| `cat file` | Показать содержимое файла | `cat file.txt` |
| `less file` | Просмотр с прокруткой | `less file.txt` |
| `more file` | Просмотр с прокруткой (базовый) | `more file.txt` |
| `head -n file` | Первые N строк | `head -10 file.txt` |
| `tail -n file` | Последние N строк | `tail -10 file.txt` |
| `tail -f file` | Отслеживать изменения файла | `tail -f /var/log/syslog` |
| `wc file` | Подсчёт строк, слов, символов | `wc file.txt` |
| `wc -l file` | Только строки | `wc -l file.txt` |
| `wc -w file` | Только слова | `wc -w file.txt` |
| `wc -c file` | Только символы | `wc -c file.txt` |

### Поиск в тексте
| Команда | Описание | Пример |
|---------|----------|--------|
| `grep pattern file` | Поиск шаблона в файле | `grep "error" log.txt` |
| `grep -i pattern file` | Регистронезависимый поиск | `grep -i "error" log.txt` |
| `grep -v pattern file` | Инвертированный поиск | `grep -v "info" log.txt` |
| `grep -n pattern file` | Показать номера строк | `grep -n "error" log.txt` |
| `grep -c pattern file` | Подсчитать совпадения | `grep -c "error" log.txt` |
| `grep -r pattern dir` | Рекурсивный поиск | `grep -r "error" /var/log` |
| `grep -E pattern file` | Расширенные регулярные выражения | `grep -E "error|warning" log.txt` |

### Обработка текста
| Команда | Описание | Пример |
|---------|----------|--------|
| `sort file` | Отсортировать строки | `sort file.txt` |
| `sort -n file` | Числовая сортировка | `sort -n numbers.txt` |
| `sort -r file` | Обратная сортировка | `sort -r file.txt` |
| `uniq file` | Удалить дубликаты | `sort file.txt | uniq` |
| `uniq -c file` | Подсчитать дубликаты | `sort file.txt | uniq -c` |
| `cut -fN file` | Вырезать N-е поле | `cut -f1 file.txt` |
| `cut -d: -fN file` | Использовать другой разделитель | `cut -d: -f1 /etc/passwd` |
| `cut -cN-M file` | Вырезать символы с N по M | `cut -c1-5 file.txt` |

## Продвинутая обработка текста

### sed (Stream Editor)
| Команда | Описание | Пример |
|---------|----------|--------|
| `sed 's/old/new/g' file` | Заменить текст | `sed 's/error/ERROR/g' log.txt` |
| `sed -i 's/old/new/g' file` | Заменить в файле | `sed -i 's/error/ERROR/g' log.txt` |
| `sed '/pattern/d' file` | Удалить строки с шаблоном | `sed '/^#/d' config.txt` |
| `sed -n 'N,Mp' file` | Показать строки с N по M | `sed -n '5,10p' file.txt` |
| `sed 'N,Md' file` | Удалить строки с N по M | `sed '5,10d' file.txt` |
| `sed 's/^/prefix/' file` | Добавить префикс | `sed 's/^/> /' file.txt` |
| `sed 's/$/suffix/' file` | Добавить суффикс | `sed 's/$/.txt/' file.txt` |

### awk
| Команда | Описание | Пример |
|---------|----------|--------|
| `awk '{print $1}' file` | Показать первый столбец | `awk '{print $1}' file.txt` |
| `awk -F: '{print $1}' file` | Использовать разделитель | `awk -F: '{print $1}' /etc/passwd` |
| `awk 'NR==N' file` | Показать N-ю строку | `awk 'NR==5' file.txt` |
| `awk 'NR>=N && NR<=M' file` | Строки с N по M | `awk 'NR>=5 && NR<=10' file.txt` |
| `awk '$N > value' file` | Условие по столбцу | `awk '$3 > 100' file.txt` |
| `awk '{sum+=$N} END {print sum}' file` | Сумма столбца | `awk '{sum+=$1} END {print sum}' file.txt` |
| `awk 'NF==N' file` | Строки с N полями | `awk 'NF==3' file.txt` |
| `awk '{print NR, $0}' file` | Добавить номер строки | `awk '{print NR, $0}' file.txt` |

## Комбинирование команд

### Использование pipe (|)
| Команда | Описание | Пример |
|---------|----------|--------|
| `cmd1 | cmd2` | Передать вывод cmd1 в cmd2 | `ps aux | grep nginx` |
| `cmd1 | cmd2 | cmd3` | Цепочка команд | `cat file.txt | grep error | wc -l` |
| `cmd | tee file` | Сохранить и передать дальше | `ls -la | tee filelist.txt | grep ".txt"` |

### Использование xargs
| Команда | Описание | Пример |
|---------|----------|--------|
| `cmd | xargs cmd2` | Передать аргументы | `ls *.txt | xargs rm` |
| `cmd | xargs -I {} cmd2` | Заменить {} | `find . -name "*.jpg" | xargs -I {} cp {} /backup/` |
| `cmd | xargs -n N cmd2` | N аргументов за раз | `echo 1 2 3 4 5 | xargs -n 2 echo` |
| `cmd | xargs -p cmd2` | Запрос подтверждения | `find . -name "*.tmp" | xargs -p rm` |

## Регулярные выражения

### Базовые символы
| Символ | Описание | Пример |
|--------|----------|--------|
| `.` | Любой символ | `grep "h.t" file.txt` |
| `*` | Ноль или более повторений | `grep "a*b" file.txt` |
| `+` | Одно или более повторений | `grep -E "a+b" file.txt` |
| `?` | Ноль или одно повторение | `grep -E "a?b" file.txt` |
| `^` | Начало строки | `grep "^error" file.txt` |
| `$` | Конец строки | `grep "error$" file.txt` |
| `[]` | Любой символ из скобок | `grep "[aeiou]" file.txt` |
| `[^]` | Любой символ кроме указанных | `grep "[^aeiou]" file.txt` |
| `\` | Экранирование спецсимвола | `grep "\." file.txt` |

### Классы символов
| Класс | Описание | Пример |
|-------|----------|--------|
| `[[:alpha:]]` | Буквы | `grep "[[:alpha:]]" file.txt` |
| `[[:digit:]]` | Цифры | `grep "[[:digit:]]" file.txt` |
| `[[:alnum:]]` | Буквы и цифры | `grep "[[:alnum:]]" file.txt` |
| `[[:space:]]` | Пробельные символы | `grep "[[:space:]]" file.txt` |
| `[[:lower:]]` | Строчные буквы | `grep "[[:lower:]]" file.txt` |
| `[[:upper:]]` | Прописные буквы | `grep "[[:upper:]]" file.txt` |

### Квантификаторы
| Квантификатор | Описание | Пример |
|---------------|----------|--------|
| `{n}` | Ровно n повторений | `grep -E "a{3}" file.txt` |
| `{n,}` | n или более повторений | `grep -E "a{3,}" file.txt` |
| `{n,m}` | от n до m повторений | `grep -E "a{2,4}" file.txt` |

## Полезные однострочники

### Анализ системы
```bash
# 10 самых больших файлов
find . -type f -exec ls -lah {} \; | sort -rh | head -n 10

# Процессы, потребляющие больше всего памяти
ps aux --sort=-%mem | head -n 10

# Процессы, потребляющие больше всего CPU
ps aux --sort=-%cpu | head -n 10

# Свободное место на дисках
df -h | grep -vE '^Filesystem|tmpfs|cdrom' | awk '{print $5 " " $1}'

# Подключения к сети
netstat -ntu | awk 'NR>1 {print $5}' | cut -d: -f1 | sort | uniq -c | sort -nr
```

### Работа с файлами
```bash
# Поиск и замена в файлах
find . -name "*.txt" -exec sed -i 's/old/new/g' {} \;

# Удаление пустых файлов
find . -type f -empty -delete

# Переименование файлов
for file in *.txt; do mv "$file" "${file%.txt}.bak"; done

# Создание резервной копии
tar -czf backup_$(date +%Y%m%d_%H%M%S).tar.gz /path/to/directory
```

### Анализ логов
```bash
# Подсчёт ошибок в логе
grep -c "ERROR" logfile.txt

# Уникальные IP-адреса в логе
grep -oE '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' access.log | sort | uniq

# Ошибки за последний час
find /var/log -name "*.log" -mmin -60 -exec grep -c "ERROR" {} \;

# Самые частые запросы
awk '{print $7}' access.log | sort | uniq -c | sort -nr | head -n 10
