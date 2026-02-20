```bash
curl -X PUT http://localhost:5005/user/1/name \
  -H "Content-Type: application/json" \
  -d '{"name": "Иван"}'

curl http://localhost:5005/user/1
```
