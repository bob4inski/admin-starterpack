# Database intro

### Подходы к обработке
Какие виды нагрузки на БД вы можете представить?


OLTP - Online Transaction Processing
Для быстрых точечных запросов и вставках

OLAP - Online Analytical Processing

Будем на примере с постгресом

### С чего начинается работа с БД
- подключение
- подключение большого количества пользователей

### А как подключиться к базе? HBA conf

```bash
root@bob4inski-1:~# psql
psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: FATAL:  role "root" does not exist
root@bob4inski-1:~#
```

### MVCC Что такое транзакции

### Уровни изоляции

### Автовакуум и зачем нужен

### Уровни изоляции БД

#### Как выбирать даныне

- простое
- бекапы
- встроенные шарды


### Эксплуатация
### HBA conf
### Тунинг параметров в БД
### Бекапы
###

```sql
CREATE TABLE mvcc_test (
    id serial PRIMARY KEY,
    value text
);

INSERT INTO mvcc_test (value) VALUES ('test');
SELECT xmin, xmax, id, value FROM mvcc_test;

create role readonly with login;
grant connect on database testdb to readonly;
grant select, usage  on schema testnm to readonly;
grant select on all tables in schema testnm to readonly;


show config_file;

SELECT * from  pg_settings
WHERE pending_restart;

SELECT name, context FROM pg_settings
WHERE context = 'sighup';

SELECT pg_reload_conf();
