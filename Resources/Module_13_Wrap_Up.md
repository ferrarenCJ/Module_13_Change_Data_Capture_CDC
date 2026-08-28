# Module 13: Wrap-Up

## Module Overview

Module 13 focused on Change Data Capture (CDC), container automation, database initialization, and time-loop scheduling in Python.

The module combined database technologies, Docker containers, and Python automation to build a working CDC system capable of propagating changes from a source database to multiple target databases.

---

# Learning Outcomes Achieved

## 1. Understand Change Data Capture (CDC)

CDC is a software process used to identify and propagate changes made to a source database.

### CDC Components

#### Change Detection

Identifies when data has changed.

#### Change Capture

Records details about the change.

#### Change Propagation

Distributes the change to downstream systems.

---

## 2. Understand CDC Methods

Methods explored included:

### Audit Columns

Examples:

```text
created_time
updated_time
changed_time
```

### Periodic Queries

Timestamp-based polling.

### Database Triggers

Database-generated change events.

### Dual Writes

Applications write to multiple systems simultaneously.

### Network-Level Sniffing

Capturing database changes from network activity.

---

# Container Automation

Python was used to automate Docker container management.

## Python Libraries

```python
import os
import sys
```

### Create Containers

```bash
docker run
```

### Stop Containers

```bash
docker stop
```

### Delete Containers

```bash
docker rm
```

### Benefits

- Automation
- Repeatability
- Reduced errors
- Faster deployment

---

# Time Loops

Python timers and loops were used to simulate periodic activity.

## Libraries

```python
import threading
import time
```

### Timer

```python
threading.Timer()
```

### Delay Execution

```python
time.sleep()
```

### Cancel Timer

```python
timer.cancel()
```

### Purpose

- Automated execution
- CDC polling
- System testing
- Database simulation

---

# Database Initialization

## MySQL

Initialization required:

```sql
CREATE DATABASE
CREATE TABLE
```

Database:

```text
pluto
```

Table:

```text
posts
```

---

## MongoDB

Initialization not required.

Collections are created automatically.

---

## Redis

Initialization not required.

Data is stored immediately.

---

## Cassandra

Initialization required.

Created:

```text
Keyspace: stamps
```

Table:

```text
posts
```

---

# CDC Pipeline Built in Module 13

## Activity 13.3

CDC Pipeline:

```text
MySQL
   │
   ▼
MongoDB
```

---

## Activity 13.4

CDC Pipeline:

```text
MySQL
   │
   ├── MongoDB
   │
   └── Redis
```

---

## Activity 13.5

Final CDC Pipeline:

```text
MySQL
   │
   ├── MongoDB
   │
   ├── Redis
   │
   └── Cassandra
```

---

# Activities Completed

## Activity 13.1

Creating and Deleting Containers Using Python

Created:

- MySQL
- MongoDB
- Redis
- Cassandra

containers programmatically.

---

## Activity 13.2

Implementing Time Loops

Implemented:

- Nested dictionaries
- Timers
- Delayed execution
- Timer cancellation

---

## Activity 13.3

Performing CDC and Initializing MySQL and MongoDB Containers

Built the first CDC pipeline.

---

## Activity 13.4

Performing CDC and Initializing a Redis Database Container

Added Redis support.

---

## Activity 13.5

Performing CDC and Initializing a Cassandra Database Container

Completed the final CDC architecture.

---

# Key Technical Skills Gained

## Python

- os
- sys
- threading
- time

---

## Docker

- Container creation
- Container deletion
- Container lifecycle management

---

## Databases

### MySQL

Relational database.

### MongoDB

Document database.

### Redis

Key-value store.

### Cassandra

Distributed NoSQL database.

---

## CDC

- Detect changes
- Capture changes
- Propagate changes
- Synchronize multiple databases

---

# Real-World Applications

CDC can be used for:

- Data warehouses
- Data lakes
- Event-driven architectures
- Analytics platforms
- Dashboard refresh processes
- Master data management
- Operational reporting
- Microservices synchronization

---

# Final Takeaways

- CDC enables synchronization of changes across multiple systems.
- Python can automate both container management and database operations.
- Time loops provide a mechanism for periodic CDC execution.
- Different databases require different initialization strategies.
- A single source database can propagate changes to multiple destinations.
- Docker containers provide an isolated and reproducible environment for database deployments.
- Module 13 culminated in a complete multi-database CDC system with MySQL