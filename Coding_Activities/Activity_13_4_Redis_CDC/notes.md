# Activity 13.4 Notes

## Learning Outcomes

- Initialize database containers
- Perform CDC on multiple containers
- Extend CDC architecture using Redis
- Use timers to automate synchronization

---

## Activity Summary

Starting Point:

```text
MySQL
   │
   ▼
MongoDB
```

Activity 13.4 adds:

```text
Redis
```

Result:

```text
MySQL
   │
   ▼
MongoDB
   │
   ▼
Redis
```

---

## Redis Container

Docker Command:

```bash
docker run -p 6379:6379 --name some-redis -d redis
```

Delete Command:

```python
delete('some-redis')
```

---

## Redis Database Operations

### Write

Store latest timestamp.

```python
client.mset({
    "LastInsertDate":
        f"{str(stamps[0])}"
})
```

---

### Read

Retrieve latest timestamp.

```python
client.get("LastInsertDate")
```

---

### Delete

Remove timestamp.

```python
client.delete("LastInsertDate")
```

---

## Scheduler Modifications

### Import Redis

```python
import redisdb
```

---

### Clearout Function

```python
redisdb.delete()
```

---

### Redis Function

```python
def redis():

    stamps = mysqldb.read()

    redisdb.write(stamps)
```

---

### Verify Function

```python
lastInsertDate = redisdb.read()

print(
    f"Data in Redis: "
    f"LastInsertDate = "
    f"{lastInsertDate.decode('utf-8')}"
)
```

---

### Timeloop Function

```python
redis()
```

added after:

```python
mongo()
```

---

## Scheduler Output

Expected:

```text
--- LOOP ---

Data in mysql:
2026-08-28 10:35:12

Data in mongo:
2026-08-28 10:35:12

Data in Redis:
LastInsertDate = 2026-08-28 10:35:12
```

---

## Validation

### Verify MySQL

```sql
SHOW DATABASES;

USE pluto;

SHOW TABLES;

DESCRIBE posts;
```

Expected Table:

```text
posts
```

Columns:

```text
id
stamp
```

---

### Verify Redis

Check:

```python
redisdb.read()
```

Expected:

```text
LastInsertDate
```

contains latest MySQL timestamp.

---

## Screenshots Collected

### Step 1

Activity13.4 folder

### Step 2

Redis create code

### Step 3

Container creation execution

### Step 4

Three containers running

### Step 5

Database initialization

### Step 6

Redis delete code

### Step 7

redisdb.py

### Step 8a

Import redisdb

### Step 8b

clearout function

### Step 8c

redis function

### Step 8d

verify function

### Step 8e

timeloop modification

### Step 9

Scheduler output

### Step 10

Container deletion

### Step 11

Containers removed

---

## Key Concepts Learned

- Redis does not require initialization.
- Redis is used as a lightweight key-value store.
- CDC can propagate data to multiple target databases.
- Timer-based loops automate synchronization.
- MySQL remains the source of truth.
- MongoDB and Redis act as CDC destinations.