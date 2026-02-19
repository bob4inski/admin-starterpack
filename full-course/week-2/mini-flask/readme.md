### Как поднять

```bash
docker-compose up
```

## Иньекция
```bash
curl 'http://localhost:5005/user/get?id=1%20or%201=1'
```

```bash
# Подключиться к админке
psql -h localhost -p 6432 -U postgres pgbouncer

# Внутри консоли:
pgbouncer=# SHOW POOLS;
pgbouncer=# SHOW DATABASES;
pgbouncer=# SHOW STATS;
pgbouncer=# SHOW CLIENTS;
pgbouncer=# SHOW SERVERS;
```
