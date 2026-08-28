# Redis Commands Cheat Sheet

## Connect to Redis

```bash
docker exec -it some-redis redis-cli
```

---

## Set Value

```bash
SET LastInsertDate "2026-08-28"
```

---

## Get Value

```bash
GET LastInsertDate
```

---

## Delete Key

```bash
DEL LastInsertDate
```

---

## Show All Keys

```bash
KEYS *
```

---

## Database Size

```bash
DBSIZE
```

---

## Clear Database

```bash
FLUSHDB
```

---

# Python Redis Connection

```python
import redis

client = redis.Redis(
    host='localhost',
    port=6379,
    db=0
)
```

---

## Write Data

```python
client.mset({
    "LastInsertDate":
        "2026-08-28"
})
```

---

## Read Data

```python
client.get(
    "LastInsertDate"
)
```

---

## Delete Data

```python
client.delete(
    "LastInsertDate"
)
```