# Final Assignment 13.1: Change Data Capture (CDC)

## Overview

This assignment demonstrates the implementation of Change Data Capture (CDC) concepts using Python, Docker, MySQL, MongoDB, Redis, and Cassandra.

The assignment is divided into two parts:

### Part 1

Create database containers programmatically using Python.

### Part 2

Initialize databases and implement a simple CDC workflow using MySQL and MongoDB with a scheduler based on Python time loops.

---

# Learning Outcomes

- Create and delete containers using Python
- Implement time loops
- Initialize database containers
- Perform CDC across multiple database platforms

---

# Technologies Used

- Python 3.x
- Docker Desktop
- MySQL
- MongoDB
- Redis
- Cassandra
- PyMySQL
- PyMongo
- threading.Timer

---

# Part 1: Container Creation

## MySQL Container

### File

```text
my_sql_container.py
```

### Container

```text
final_mysql_container
```

### Port Mapping

```text
5600:3306
```

---

## MongoDB Container

### File

```text
my_mongo_container.py
```

### Container

```text
final_mongo_container
```

### Port Mapping

```text
1800:27017
```

---

## Redis Container

### File

```text
my_redis_container.py
```

### Container

```text
final_redis_container
```

### Port Mapping

```text
2400:6379
```

---

## Cassandra Container

### File

```text
my_cassandra_container.py
```

### Container

```text
final_cassandra_container
```

### Port Mapping

```text
1000:9042
```

---

# Part 2: CDC Implementation

## container.py

Responsible for:

- Creating containers
- Deleting containers
- Initializing MySQL database

Supported parameters:

```bash
python container.py -create
python container.py -init
python container.py -delete
```

---

## Database Initialization

### Database

```text
pluto
```

### Table

```text
posts
```

### Structure

```sql
CREATE TABLE posts (
    id VARCHAR(36),
    stamp VARCHAR(20)
)
```

---

## mysqldb.py

Functions:

- Connect to MySQL
- Insert records
- Read records

Sample data:

```text
UUID
Timestamp
```

---

## mongodb.py

Functions:

- Connect to MongoDB
- Insert documents
- Verify database communication

Database:

```text
pluto
```

Collection:

```text
posts
```

---

## scheduler.py

Controller for CDC simulation.

Uses:

```python
from threading import Timer
```

to perform operations at regular intervals.

Workflow:

```text
Insert Data
↓
Read Data
↓
Display Status
↓
Wait
↓
Repeat
```

---

# CDC Architecture

```text
                 MySQL
                    │
                    ▼
                MongoDB

                Redis

              Cassandra
```

MySQL