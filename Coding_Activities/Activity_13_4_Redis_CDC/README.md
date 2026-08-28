# Activity 13.4: Performing CDC and Initializing a Redis Database Container

## Objective

Extend the CDC system developed in Activity 13.3 by adding Redis as an additional target database.

The CDC pipeline now propagates data from MySQL to:

- MongoDB
- Redis

---

## Technologies Used

- Python
- Docker
- MySQL
- MongoDB
- Redis
- PyMySQL
- PyMongo
- Redis Python Client
- Threading Timer

---

## Files

### container.py

Responsible for:

- Creating containers
- Deleting containers
- Initializing MySQL

### mysqldb.py

Used to:

- Write timestamps to MySQL
- Read timestamps from MySQL
- Delete table contents

### mongodb.py

Used to:

- Write data to MongoDB
- Read data from MongoDB
- Remove collection contents

### redisdb.py

Used to:

- Store the most recent timestamp
- Read the last timestamp
- Delete Redis data

### scheduler.py

Controls CDC processing using a timer-based loop.

---

## CDC Architecture

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

## Redis Data Structure

Redis stores