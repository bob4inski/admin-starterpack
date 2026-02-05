# Практическое руководство: Установка Arch Linux с RAID массивом

## Введение

Это руководство проведет вас через процесс установки Arch Linux с программным RAID1 массивом для обеспечения отказоустойчивости. Мы будем использовать два виртуальных диска для создания зеркального массива.

## Подготовка

### Требования
- Виртуальная машина с 2 дисками по 20GB каждый
- Доступ к интернету
- Базовые знания командной строки Linux

### Создание виртуальной машины
1. Создайте новую виртуальную машину в VirtualBox/VMware/KVM
2. Настройте 2 виртуальных диска по 20GB каждый
3. Выделите не менее 2GB RAM
4. Настройте сетевой адаптер для доступа в интернет

## Процесс установки

### Шаг 1: Загрузка с установочного образа
1. Скачайте образ Arch Linux с [официального сайта](https://archlinux.org/download/)
2. Загрузите виртуальную машину с этого образа
3. Выберите "Boot Arch Linux (x86_64)" в меню загрузки

### Шаг 2: Проверка интернет-соединения
```bash
# Проверка подключения
ping -c 4 archlinux.org

# Если нет подключения, настройте сеть
ip link
# Найдите ваш сетевой интерфейс (например, eth0 или enp0s3)
dhcpcd eth0
```

### Шаг 3: Обновление системного времени
```bash
timedatectl set-ntp true
timedatectl status
```

### Шаг 4: Разметка дисков
```bash
# Определите имена дисков
lsblk

# Разметка первого диска (/dev/sda)
fdisk /dev/sda
# Создайте следующие разделы:
# 1: 512MB, тип EFI (если UEFI) или BIOS boot (если BIOS)
# 2: 2GB, тип Linux swap
# 3: Остальное пространство, тип Linux RAID

# Разметка второго диска (/dev/sdb)
fdisk /dev/sdb
# Создайте аналогичные разделы:
# 1: 512MB, тип EFI (если UEFI) или BIOS boot (если BIOS)
# 2: 2GB, тип Linux swap
# 3: Остальное пространство, тип Linux RAID

# Проверка разметки
fdisk -l
```

### Шаг 5: Создание RAID массивов
```bash
# Установка mdadm
pacman -Sy mdadm

# Создание RAID1 для корневой файловой системы
mdadm --create --verbose /dev/md0 --level=mirror --raid-devices=2 /dev/sda3 /dev/sdb3

# Проверка состояния массива
cat /proc/mdstat
watch cat /proc/mdstat  # наблюдение за процессом синхронизации
```

### Шаг 6: Форматирование разделов
```bash
# Форматирование boot раздела (только на первом диске)
mkfs.fat -F32 /dev/sda1  # для UEFI
# или
mkfs.ext4 /dev/sda1      # для BIOS

# Форматирование swap разделов
mkswap /dev/sda2
mkswap /dev/sdb2

# Активация swap
swapon /dev/sda2
swapon /dev/sdb2

# Форматирование RAID массива
mkfs.ext4 /dev/md0
```

### Шаг 7: Монтирование файловых систем
```bash
# Монтирование корневого раздела
mount /dev/md0 /mnt

# Создание директории для boot
mkdir /mnt/boot

# Монтирование boot раздела
mount /dev/sda1 /mnt/boot
```

### Шаг 8: Установка базовой системы
```bash
# Установка базовых пакетов
pacstrap /mnt base linux linux-firmware

# Установка дополнительных полезных пакетов
pacstrap /mnt base-devel nano vim networkmanager
```

### Шаг 9: Настройка системы
```bash
# Генерация fstab
genfstab -U /mnt >> /mnt/etc/fstab

# Проверка fstab
cat /mnt/etc/fstab

# Переход в установленную систему
arch-chroot /mnt
```

### Шаг 10: Базовая конфигурация
```bash
# Установка часового пояса
ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime
hwclock --systohc

# Настройка локализации
sed -i 's/#ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen
locale-gen
echo "LANG=ru_RU.UTF-8" > /etc/locale.conf

# Настройка клавиатуры
echo "KEYMAP=ru" > /etc/vconsole.conf

# Настройка имени хоста
echo "arch-raid" > /etc/hostname

# Настройка hosts
cat > /etc/hosts << EOF
127.0.0.1   localhost
::1         localhost
127.0.1.1   arch-raid.localdomain arch-raid
EOF
```

### Шаг 11: Настройка загрузчика
```bash
# Установка пакетов для загрузчика
pacman -S grub efibootmgr

# Установка GRUB
grub-install --target=i386-pc /dev/sda
grub-install --target=i386-pc /dev/sdb

# Для UEFI систем:
# grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB

# Настройка mdadm в initramfs
echo "BINARIES=(/usr/bin/mdadm)" >> /etc/mkinitcpio.conf
echo "FILES=(/etc/mdadm.conf)" >> /etc/mkinitcpio.conf

# Создание конфигурации mdadm
mdadm --detail --scan > /etc/mdadm.conf

# Пересборка initramfs
mkinitcpio -p linux

# Генерация конфигурации GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```

### Шаг 12: Настройка пользователей и сетевых служб
```bash
# Установка пароля root
passwd

# Создание пользователя
useradd -m -G wheel,storage,power -s /bin/bash admin
passwd admin

# Настройка sudo
pacman -S sudo
visudo
# Раскомментируйте строку: %wheel ALL=(ALL) ALL

# Включение сетевой службы
systemctl enable NetworkManager
systemctl start NetworkManager
```

### Шаг 13: Завершение установки
```bash
# Выход из chroot
exit

# Размонтирование файловых систем
umount -R /mnt

# Перезагрузка
reboot
```

## Проверка и тестирование

### Проверка RAID массива
```bash
# Проверка состояния RAID
cat /proc/mdstat
mdadm --detail /dev/md0

# Проверка файловой системы
df -h
lsblk
```

### Тестирование отказоустойчивости
```bash
# Имитация сбоя диска
mdadm --fail /dev/md0 /dev/sda3

# Проверка состояния
cat /proc/mdstat

# Удаление сбойного диска
mdadm --remove /dev/md0 /dev/sda3

# Добавление нового диска (замените /dev/sdc3 на реальный раздел)
mdadm --add /dev/md0 /dev/sdc3

# Наблюдение за восстановлением
watch cat /proc/mdstat
```

## Возможные проблемы и решения

### Проблема: RAID массив не собирается после перезагрузки
**Решение**: Убедитесь, что mdadm.conf правильно настроен и включен в initramfs

### Проблема: GRUB не видит RAID массив
**Решение**: Установите GRUB на оба диска и убедитесь, что mdadm включен в initramfs

### Проблема: Синхронизация RAID занимает слишком много времени
**Решение**: Это нормально для первоначальной синхронизации. Можно ускорить процесс:
```bash
echo 100000 > /proc/sys/dev/raid/speed_limit_min
echo 1000000 > /proc/sys/dev/raid/speed_limit_max
```

## Дополнительные настройки

### Настройка уведомлений о состоянии RAID
```bash
# Настройка email уведомлений
echo "MAILADDR admin@example.com" >> /etc/mdadm.conf
```

### Настройка регулярной проверки RAID
```bash
# Создание скрипта для проверки
cat > /etc/cron.weekly/raid-check << EOF
#!/bin/bash
/usr/sbin/mdadm --detail --test /dev/md0
EOF

chmod +x /etc/cron.weekly/raid-check
```

## Полезные команды для работы с RAID

| Команда | Описание |
|---------|----------|
| `cat /proc/mdstat` | Показать статус всех RAID массивов |
| `mdadm --detail /dev/md0` | Детальная информация о RAID массиве |
| `mdadm --fail /dev/md0 /dev/sda3` | Пометить диск как сбойный |
| `mdadm --remove /dev/md0 /dev/sda3` | Удалить диск из массива |
| `mdadm --add /dev/md0 /dev/sda3` | Добавить диск в массив |
| `mdadm --grow /dev/md0 --raid-devices=3` | Увеличить количество дисков в массиве |

## Заключение

После выполнения этих шагов у вас будет работающая система Arch Linux с RAID1 массивом для корневой файловой системы. Это обеспечит отказоустойчивость и защиту данных от сбоя одного из дисков.

## Домашнее задание

1. Создайте скрипт автоматизации установки Arch Linux с RAID
2. Исследуйте различия между программным и аппаратным RAID
3. Изучите другие уровни RAID (0, 5, 6, 10) и их применение
4. Подготовьте отчет о преимуществах и недостатках использованного решения
