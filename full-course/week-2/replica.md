```bash
# root@bob4inski-1:~# cat /etc/postgresql/16/main/conf.d/replica.conf

listen_addresses = '*'
wal_level = replica
max_wal_senders = 5
wal_keep_size = 128MB
hot_standby = on

# /etc/postgresql/16/main/pg_hba.conf
# IPv4 local connections:
host    all             all             127.0.0.1/32            scram-sha-256
# IPv6 local connections:
host    all             all             ::1/128                 scram-sha-256
# Allow replication connections from localhost, by a user with the
# replication privilege.
host    replication   repuser         10.130.0.4/32      trust

local   replication     all                                     peer
host    replication     all             127.0.0.1/32            scram-sha-256
host    replication     all             ::1/128                 scram-sha-256
# root@bob4inski-1:~#
```

```bash
pg_basebackup -h 10.130.0.12 -D /var/lib/postgresql/16/main -U repuser -P -R

```
