# admin-starterpack
База для начинающего одмена

Если будут вопросы, то пишите https://t.me/bob4inskii

### Небольшой гайд по разделам и что стоит учить как админу

В каждой папке исходя из названия будут лежать небольшие кусочки лекций с заданиями
В самом репозитории я еще не навел красоту, так что буду дополнять его по пути
Также по каждому разделу позднее добавлю список работ которые можно сделать чтобы прокачаться самому


#### Общие задания которые можно попробовать потыкать и сделать (в порядке усложнения)
#### Собрать свой дебиановский пакет с приложением на python3 которое позволит запускать
Задачка висит в [папке](./Debian_package/readme.md)

##### Использование SSL в nginx
1. Взять какое-нибудь dns имя на https://www.duckdns.org/domains
2. Выписать самоподписный сертификат https://pastebin.com/xUX6aCcF
3. Положить сертификат к nginx https://nginx.org/en/docs/http/configuring_https_servers.html
4. Настроить редирект с http -> https (80 -> 443) https://stackoverflow.com/questions/62307281/redirect-http-to-https-with-nginx

#### Системы управления конфигурациями
Лекция: https://www.youtube.com/watch?v=_8N6igbd-i4
1. Установить Ansible https://docs.ansible.com/
    - [Как правильно писать ансибл](https://docs.ansible.com/ansible/2.8/user_guide/playbooks_best_practices.html)
    - Стоит начать с [организации пространства](https://docs.ansible.com/ansible/2.8/user_guide/playbooks_best_practices.html#content-organization)
    - примеры можно посмотреть тут https://github.com/bob4inski/ansible
        На этих примерах можно понять как и что необходимо для работы ансибла
2. Потыкать что можно делать в самом ansible
3. С помощью ansible установить nginx на виртуалку/свой хост
4. Если хочется более прикольных заданий по ансиблу,

#### Системы управления конфигурациями part 2

1. Установить терраформ и на стартовый грант в yandex-cloud завести себе виртуалку https://yandex.cloud/ru/docs/tutorials/infrastructure-management/terraform-quickstart
2. Примеры конфигурации скорее там есть, но при надобности могу дополниь репозиторий


Дальше стоит посмотреть https://www.youtube.com/watch?v=S-OvD6ShZOM

#### K8s - тут я честно дам копипасту, которую делал раньше сам
Полезная лекция:
    - репо https://github.com/bob4inski/gpn-k8s-lessons
    - Для управления контейнерами часто используют helm чтобы делать все одной командой https://habr.com/ru/articles/726636/
    - Попробовать развернуть приложение полностью в качестве deployment

#### Мониторинг

Лекция https://www.youtube.com/watch?v=_GpPUf9Yeg0

Почитать про инструменты:
- prometheus https://prometheus.io/
Система, которая может собирать метрики и хранить в своей базке
Условно есть сервер, который принимает данные от воркеров, которые их каким-либо образом собирают

- grafana https://grafana.com/
Отрисовка данных из любого ресурса

- zabbix https://www.zabbix.com/
prometheus + grafana, но в другом соусе

Задание:
0. В контейнере или серисом поднять у себя prometheus и увидеть его фронт
1. установить на хост https://github.com/prometheus/node_exporter
2. Настроить сборку метрик с хоста https://prometheus.io/docs/guides/node-exporter/
3. Установить графану и в плагинах поставить отрисовку метрик из прометеуса
4. Построить дашборд о потреблении ресурсов хоста в графане
5. Найти/собрать nginx с vts exporter https://github.com/hnlq795/nginx-vts-exporter
6. Проделать п.2-п.4 для отрисовки метрик nginx (к примеру хочу увидеть сколько запросов приходит и какой процент ошибок)


### INFO
Если вам этого мало, или хотите чет проверить - пишите в тг)



