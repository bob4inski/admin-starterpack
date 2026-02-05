#!/bin/bash

# Скрипт для создания структуры директорий курса
# Использование: ./day1-scripts.sh

echo "Создание структуры директорий для курса системного администрирования..."

# Основная директория курса
COURSE_DIR="admin-course"
mkdir -p $COURSE_DIR

# Создание директорий для каждой недели
for week in {1..4}; do
    mkdir -p "$COURSE_DIR/week$week"

    # Создание директорий для каждого дня недели
    for day in {1..7}; do
        mkdir -p "$COURSE_DIR/week$week/day$day"
        mkdir -p "$COURSE_DIR/week$week/day$day/lecture"
        mkdir -p "$COURSE_DIR/week$week/day$day/practice"
        mkdir -p "$COURSE_DIR/week$week/day$day/homework"
    done
done

# Создание директорий для дополнительных материалов
mkdir -p "$COURSE_DIR/resources"
mkdir -p "$COURSE_DIR/scripts"
mkdir -p "$COURSE_DIR/configs"

echo "Структура директорий создана успешно!"
echo "Основная директория курса: $COURSE_DIR"

# Создание файла README с описанием структуры
cat > "$COURSE_DIR/README.md" << EOF
# Структура курса системного администрирования

## Описание директорий

- \`weekX/\` - материалы X-й недели обучения
  - \`dayY/\` - материалы Y-го дня недели
    - \`lecture/\` - лекционные материалы
    - \`practice/\` - практические задания
    - \`homework/\` - домашние задания

- \`resources/\` - дополнительные ресурсы и материалы
- \`scripts/\` - полезные скрипты
- \`configs/\` - конфигурационные файлы

## Навигация

Для быстрой навигации по директориям курса можно использовать алиасы:

\`\`\`bash
alias admin="cd /path/to/admin-course"
alias week1="cd /path/to/admin-course/week1"
# и так далее для каждой недели
\`\`\`
EOF

echo "Файл README.md создан в директории $COURSE_DIR"
