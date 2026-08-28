# Module 13 - Video 13.11 Notes
# CDC: Connecting and Writing to a Database Using Redis and Cassandra

## Overview

Video 13.11 concludes the CDC architecture introduced in Module 13 by extending the existing MySQL → MongoDB pipeline to include Redis and Cassandra.

At this point in the module, a CDC process has already been implemented between:

```text
MySQL
   │
   ▼
MongoDB
```

The remaining task is to expand the solution so that changes are also propagated to:

- Redis
- Cassandra

---

# Goal of the Video

The primary objective is to complete the CDC application by implementing the remaining database integrations.

Students are expected to:

1. Create Redis and Cassandra containers
2. Initialize Cassandra
3. Create Python database access modules
4. Add Redis and Cassandra logic to the scheduler
5. Verify CDC propagation across all databases

---

# Final CDC Architecture

After Activities 13.4 and 13.5, the architecture will become:

```text
               Source of Truth

                    MySQL
                       │
                       ▼

                  MongoDB
                       │
                       ▼

                    Redis
                       │
                       ▼

                 Cassandra
```

---

# Redis

## Purpose

Redis acts as an in-memory database.

Common uses include:

- Caching
- Session management
- Fast lookups
- Real-time data access

---

## Initialization

Redis does not require database initialization.

Unlike MySQL:

```sql
CREATE DATABASE
CREATE TABLE
```

Redis is immediately available once the container starts.

---

## CDC Flow

Changes propagated from MySQL can be stored in Redis.

Example:

```text
MySQL
   │
   ▼
Redis
```

---

# Cassandra

## Purpose

Cassandra is a distributed NoSQL database designed for:

- Scalability
- High availability
- Fault tolerance

---

## Initialization

Unlike Redis and MongoDB, Cassandra requires initialization.

Typical steps include:

```sql
CREATE KEYSPACE
CREATE TABLE
```

before data can be stored.

---

## CDC Flow

Changes propagated from MySQL can also be written to Cassandra.

```text
MySQL
   │
   ▼
Cassandra
```

---

# Additional Components

Students will extend:

## container.py

Add:

```python
create(...)
delete(...)
init_cassandra()
```

for Cassandra and Redis support.

---

## scheduler.py

Add:

```python
redis()
cassandra()
```

functions.

The scheduler will then execute:

```text
MySQL
MongoDB
Redis
Cassandra
```

during each loop cycle.

---

# CDC Scheduler Workflow

```text
Timer Loop
    │
    ▼

Read MySQL
    │
    ▼

Write MongoDB
    │
    ▼

Write Redis
    │
    ▼

Write Cassandra
    │
    ▼

Verify Results
    │
    ▼

Wait 5 Seconds
    │
    ▼

Repeat
```

---

# Activities Supported by This Video

## Activity 13.4

Performing CDC and Initializing Redis

Deliverables include:

- Redis container
- redisdb.py
- scheduler integration
- CDC propagation verification

---

## Activity 13.5

Performing CDC and Initializing Cassandra

Deliverables include:

- Cassandra container
- Cassandra initialization
- cassandradb.py
- scheduler integration
- CDC propagation verification

---

# Key Concepts

## Redis

```text
In-memory NoSQL database
```

### Initialization Required

```text
No
```

---

## Cassandra

```text
Distributed NoSQL database
```

### Initialization Required

```text
Yes
```

---

## CDC Expansion

Current:

```text
MySQL → MongoDB
```

Target:

```text
MySQL → MongoDB → Redis → Cassandra
```

---

## Scheduler

Responsible for:

```text
Reading
Writing
Verifying
Repeating
```

database operations.

---

# Key Takeaways

- Video 13.11 completes the CDC architecture introduced in Module 13.
- Redis and Cassandra are added to the existing CDC pipeline.
- Redis requires minimal setup and no initialization.
- Cassandra requires initialization before use.
- The scheduler will be expanded to synchronize data across all databases.
- Activities 13.4 and 13.5 build directly on Activity 13.3 by extending the existing CDC framework.