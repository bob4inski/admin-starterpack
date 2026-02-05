# Шпаргалка по командам для работы с дисками и RAID массивами

## Работа с дисками и разделами

### Информация о дисках
| Команда | Описание | Пример |
|---------|----------|--------|
| `lsblk` | Показать блочные устройства в виде дерева | `lsblk` |
| `fdisk -l` | Показать информацию о разделах | `fdisk -l` |
| `parted -l` | Показать информацию о разделах (parted) | `parted -l` |
| `df -h` | Показать смонтированные файловые системы | `df -h` |
| `du -sh` | Показать размер директории | `du -sh /home` |
| `blkid` | Показать UUID блочных устройств | `blkid` |
| `lshw -class disk` | Детальная информация о дисках | `lshw -class disk` |

### Разметка дисков
| Команда | Описание | Пример |
|---------|----------|--------|
| `fdisk /dev/sda` | Разметка диска с помощью fdisk | `fdisk /dev/sda` |
| `gdisk /dev/sda` | Разметка GPT диска с помощью gdisk | `gdisk /dev/sda` |
| `parted /dev/sda` | Разметка диска с помощью parted | `parted /dev/sda` |
| `parted /dev/sda mklabel gpt` | Создать GPT таблицу разделов | `parted /dev/sda mklabel gpt` |
| `parted /dev/sda mkpart primary 1MiB 100%` | Создать раздел | `parted /dev/sda mkpart primary 1MiB 100%` |

### Форматирование разделов
| Команда | Описание | Пример |
|---------|----------|--------|
| `mkfs.ext4 /dev/sda1` | Создать файловую систему ext4 | `mkfs.ext4 /dev/sda1` |
| `mkfs.xfs /dev/sda1` | Создать файловую систему XFS | `mkfs.xfs /dev/sda1` |
| `mkfs.btrfs /dev/sda1` | Создать файловую систему Btrfs | `mkfs.btrfs /dev/sda1` |
| `mkfs.fat -F32 /dev/sda1` | Создать FAT32 файловую систему | `mkfs.fat -F32 /dev/sda1` |
| `mkswap /dev/sda2` | Создать swap раздел | `mkswap /dev/sda2` |
| `swapon /dev/sda2` | Активировать swap раздел | `swapon /dev/sda2` |
| `swapoff /dev/sda2` | Деактивировать swap раздел | `swapoff /dev/sda2` |

### Монтирование файловых систем
| Команда | Описание | Пример |
|---------|----------|--------|
| `mount /dev/sda1 /mnt` | Смонтировать раздел | `mount /dev/sda1 /mnt` |
| `umount /mnt` | Размонтировать раздел | `umount /mnt` |
| `mount -t ext4 /dev/sda1 /mnt` | Смонтировать с указанием типа ФС | `mount -t ext4 /dev/sda1 /mnt` |
| `mount -o ro /dev/sda1 /mnt` | Смонтировать только для чтения | `mount -o ro /dev/sda1 /mnt` |
| `mount -a` | Смонтировать все из fstab | `mount -a` |
| `findmnt` | Показать смонтированные файловые системы | `findmnt` |

### Работа с fstab
| Команда | Описание | Пример |
|---------|----------|--------|
| `genfstab -U /mnt` | Сгенерировать fstab | `genfstab -U /mnt` |
| `cat /etc/fstab` | Показать содержимое fstab | `cat /etc/fstab` |
| `mount /dev/sda1` | Смонтировать из fstab | `mount /dev/sda1` |

## Работа с RAID массивами

### Создание и управление RAID
| Команда | Описание | Пример |
|---------|----------|--------|
| `mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sda1 /dev/sdb1` | Создать RAID1 | `mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sda1 /dev/sdb1` |
| `mdadm --detail /dev/md0` | Показать детальную информацию о RAID | `mdadm --detail /dev/md0` |
| `mdadm --detail --scan` | Показать информацию о всех RAID | `mdadm --detail --scan` |
| `mdadm --examine /dev/sda1` | Проверить диск на предмет RAID | `mdadm --examine /dev/sda1` |
| `mdadm --stop /dev/md0` | Остановить RAID массив | `mdadm --stop /dev/md0` |
| `mdadm --assemble /dev/md0 /dev/sda1 /dev/sdb1` | Собрать RAID массив | `mdadm --assemble /dev/md0 /dev/sda1 /dev/sdb1` |

### Управление дисками в RAID
| Команда | Описание | Пример |
|---------|----------|--------|
| `mdadm --fail /dev/md0 /dev/sda1` | Пометить диск как сбойный | `mdadm --fail /dev/md0 /dev/sda1` |
| `mdadm --remove /dev/md0 /dev/sda1` | Удалить диск из массива | `mdadm --remove /dev/md0 /dev/sda1` |
| `mdadm --add /dev/md0 /dev/sda1` | Добавить диск в массив | `mdadm --add /dev/md0 /dev/sda1` |
| `mdadm --grow /dev/md0 --raid-devices=3` | Увеличить количество дисков | `mdadm --grow /dev/md0 --raid-devices=3` |

### Мониторинг RAID
| Команда | Описание | Пример |
|---------|----------|--------|
| `cat /proc/mdstat` | Показать статус RAID массивов | `cat /proc/mdstat` |
| `watch cat /proc/mdstat` | Наблюдать за статусом RAID | `watch cat /proc/mdstat` |
| `mdadm --monitor /dev/md0` | Мониторить RAID массив | `mdadm --monitor /dev/md0` |
| `mdadm --test /dev/md0` | Проверить RAID массив | `mdadm --test /dev/md0` |

### Конфигурация mdadm
| Команда | Описание | Пример |
|---------|----------|--------|
| `mdadm --detail --scan > /etc/mdadm.conf` | Создать конфигурационный файл | `mdadm --detail --scan > /etc/mdadm.conf` |
| `cat /etc/mdadm.conf` | Показать конфигурацию | `cat /etc/mdadm.conf` |
| `echo "MAILADDR admin@example.com" >> /etc/mdadm.conf` | Настроить email уведомления | `echo "MAILADDR admin@example.com" >> /etc/mdadm.conf` |

## Работа с LVM (Logical Volume Manager)

### Физические тома (Physical Volumes)
| Команда | Описание | Пример |
|---------|----------|--------|
| `pvcreate /dev/sda1` | Создать физический том | `pvcreate /dev/sda1` |
| `pvdisplay` | Показать информацию о физических томах | `pvdisplay` |
| `pvs` | Краткая информация о физических томах | `pvs` |
| `pvremove /dev/sda1` | Удалить физический том | `pvremove /dev/sda1` |

### Группы томов (Volume Groups)
| Команда | Описание | Пример |
|---------|----------|--------|
| `vgcreate vg0 /dev/sda1 /dev/sdb1` | Создать группу томов | `vgcreate vg0 /dev/sda1 /dev/sdb1` |
| `vgdisplay` | Показать информацию о группах томов | `vgdisplay` |
| `vgs` | Краткая информация о группах томов | `vgs` |
| `vgextend vg0 /dev/sdc1` | Расширить группу томов | `vgextend vg0 /dev/sdc1` |
| `vgreduce vg0 /dev/sda1` | Уменьшить группу томов | `vgreduce vg0 /dev/sda1` |
| `vgremove vg0` | Удалить группу томов | `vgremove vg0` |

### Логические тома (Logical Volumes)
| Команда | Описание | Пример |
|---------|----------|--------|
| `lvcreate -L 10G -n lv0 vg0` | Создать логический том 10GB | `lvcreate -L 10G -n lv0 vg0` |
| `lvcreate -l 100%FREE -n lv0 vg0` | Использовать всё свободное место | `lvcreate -l 100%FREE -n lv0 vg0` |
| `lvdisplay` | Показать информацию о логических томах | `lvdisplay` |
| `lvs` | Краткая информация о логических томах | `lvs` |
| `lvextend -L +5G /dev/vg0/lv0` | Расширить логический том на 5GB | `lvextend -L +5G /dev/vg0/lv0` |
| `lvreduce -L -5G /dev/vg0/lv0` | Уменьшить логический том на 5GB | `lvreduce -L -5G /dev/vg0/lv0` |
| `lvremove /dev/vg0/lv0` | Удалить логический том | `lvremove /dev/vg0/lv0` |

### Снапшоты LVM
| Команда | Описание | Пример |
|---------|----------|--------|
| `lvcreate -L 1G -s -n snap0 /dev/vg0/lv0` | Создать снапшот | `lvcreate -L 1G -s -n snap0 /dev/vg0/lv0` |
| `lvconvert --merge /dev/vg0/snap0` | Слить снапшот с оригиналом | `lvconvert --merge /dev/vg0/snap0` |

## Проверка и восстановление файловых систем

### Проверка файловых систем
| Команда | Описание | Пример |
|---------|----------|--------|
| `fsck /dev/sda1` | Проверить файловую систему | `fsck /dev/sda1` |
| `fsck.ext4 /dev/sda1` | Проверить ext4 файловую систему | `fsck.ext4 /dev/sda1` |
| `fsck -y /dev/sda1` | Проверить с автоматическим исправлением | `fsck -y /dev/sda1` |
| `fsck -n /dev/sda1` | Проверить без исправлений | `fsck -n /dev/sda1` |
| `tune2fs -l /dev/sda1` | Показать информацию о файловой системе | `tune2fs -l /dev/sda1` |

### Дефрагментация и оптимизация
| Команда | Описание | Пример |
|---------|----------|--------|
| `e4defrag /dev/sda1` | Дефрагментировать ext4 | `e4defrag /dev/sda1` |
| `xfs_fsr /dev/sda1` | Дефрагментировать XFS | `xfs_fsr /dev/sda1` |
| `btrfs filesystem defragment /dev/sda1` | Дефрагментировать Btrfs | `btrfs filesystem defragment /dev/sda1` |

## Мониторинг состояния дисков

### SMART и здоровье дисков
| Команда | Описание | Пример |
|---------|----------|--------|
| `smartctl -a /dev/sda` | Показать SMART информацию | `smartctl -a /dev/sda` |
| `smartctl -t short /dev/sda` | Запустить короткий тест | `smartctl -t short /dev/sda` |
| `smartctl -t long /dev/sda` | Запустить длинный тест | `smartctl -t long /dev/sda` |
| `smartctl -H /dev/sda` | Показать здоровье диска | `smartctl -H /dev/sda` |

### Производительность дисков
| Команда | Описание | Пример |
|---------|----------|--------|
| `hdparm -Tt /dev/sda` | Тест производительности диска | `hdparm -Tt /dev/sda` |
| `dd if=/dev/zero of=/tmp/test bs=1G count=1 oflag=direct` | Тест записи | `dd if=/dev/zero of=/tmp/test bs=1G count=1 oflag=direct` |
| `dd if=/tmp/test of=/dev/null bs=1G count=1 iflag=direct` | Тест чтения | `dd if=/tmp/test of=/dev/null bs=1G count=1 iflag=direct` |
| `iotop` | Мониторинг дисковой активности | `iotop` |

## Уровни RAID

| Уровень | Минимум дисков | Описание | Преимущества | Недостатки |
|---------|----------------|----------|--------------|------------|
| RAID 0 | 2 | Стрипинг (без избыточности) | Максимальная производительность | Нет отказоустойчивости |
| RAID 1 | 2 | Зеркалирование | Полная отказоустойчивость | 50% эффективности |
| RAID 5 | 3 | Стрипинг с чётностью | Хорошая производительность и отказоустойчивость | Медленная запись |
| RAID 6 | 4 | Стрипинг с двойной чётностью | Высокая отказоустойчивость | Ещё медленнее запись |
| RAID 10 | 4 | Зеркалирование + стрипинг | Высокая производительность и отказоустойчивость | Сложная конфигурация |

## Типы файловых систем

| Файловая система | Особенности | Преимущества | Недостатки |
|------------------|-------------|--------------|------------|
| ext4 | Стандартная для Linux | Надёжность, стабильность | Ограничения на размер файлов |
| XFS | Высокая производительность | Отличная работа с большими файлами | Сложнее восстановление |
| Btrfs | Современная, снапшоты | Копирование при записи, сжатие | Менее зрелая |
| ZFS | Продвинутые функции | Высокая надёжность, сжатие, дедупликация | Требует много памяти |
| NTFS | Стандартная для Windows | Совместимость с Windows | Ограниченная поддержка в Linux |

## Полезные сочетания клавиш в fdisk

| Команда | Описание |
|---------|----------|
| `m` | Показать справку |
| `p` | Показать таблицу разделов |
| `n` | Создать новый раздел |
| `d` | Удалить раздел |
| `t` | Изменить тип раздела |
| `w` | Сохранить изменения и выйти |
| `q` | Выйти без сохранения |
| `a` | Сделать раздел загрузочным |
| `l` | Показать список типов разделов |

## Типы разделов

| Код | Тип | Описание |
|-----|-----|----------|
| `83` | Linux | Стандартный раздел Linux |
| `82` | Linux swap | Раздел подкачки Linux |
| `fd` | Linux RAID | Раздел для программного RAID |
| `8e` | Linux LVM | Раздел для LVM |
| `ef` | EFI System Partition | Раздел для UEFI |
| `ee` | GPT Protective MBR | Защитная MBR для GPT |
