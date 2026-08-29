# Module 13 Glossary

## Audit Columns

A Change Data Capture (CDC) technique that adds columns to a table to track when records are created or modified.

Examples:

```text
created_date
updated_date
modified_timestamp
```

Used for:

- Detecting changes
- Incremental loads
- Synchronization processes

---

## Change Data Capture (CDC)

A process used to identify, capture, and propagate changes from a source database to one or more destination systems.

CDC consists of:

1. Change Detection
2. Change Capture
3. Change Propagation

Examples of tracked events:

```text
INSERT
UPDATE
DELETE
```

---

## Change Detection

The process of identifying that a change has occurred in the source database.

Examples:

```text
New record added
Record modified
Record removed
```

---

## Change Capture

The process of recording details about a detected change.

Captured information may include:

```text
Primary Key
Timestamp
Modified Values
Operation Type
```

---

## Change Propagation

The process of sending captured changes to downstream systems.

Example:

```text
MySQL
   │
   ▼
MongoDB
Redis
Cassandra
```

---

## Controller

A software component that manages the flow of data between systems.

In Module 13:

```text
scheduler.py
```

acts as the controller.

Responsibilities:

- Read from databases
- Write to databases
- Manage CDC execution
- Schedule recurring tasks

---

## create() Function

A Python function used to create database containers.

Example:

```python
create(
    "docker run ...",
    "mysql"
)
```

Used for:

- MySQL
- MongoDB
- Redis
- Cassandra

container creation.

---

## delete() Function

A Python function used to stop and remove containers.

Example:

```python
delete("some-mysql")
```

Used for container cleanup and lifecycle management.

---

## Table Deltas

A CDC technique that identifies changes by comparing data states over time.

Used to identify:

```text
Inserted Records
Updated Records
Deleted Records
```

---

## Time Loops

A scheduling mechanism that repeatedly executes code after a specified interval.

Example:

```python
Timer(
    5,
    timeloop
).start()
```

Common uses:

- CDC polling
- Monitoring
- Automation
- Data synchronization

---

## Timer

A Python object used to delay or schedule execution of a function.

Provided by:

```python
threading
```

library.

Example:

```python
timer = threading.Timer(
    5,
    my_function
)
```

---

## timer() Method

A method from Python's `threading` module used to schedule future execution.

Syntax:

```python
threading.Timer(
    interval,
    function
)
```

Example:

```python
threading.Timer(
    5,
    timeloop
)
```

Executes:

```text
timeloop()
```

after 5 seconds.

---

# Module 13 Key Concepts

## CDC Architecture

```text
Detect
   │
   ▼
Capture
   │
   ▼
Propagate
```

---

## Source Database

In Module 13:

```text
MySQL
```

served as the source of truth.

---

## Destination Databases

Module 13 propagated data to:

```text
MongoDB
Redis
Cassandra
```

---

## Container Automation

Implemented using:

```python
os.system()
```

and Docker commands.

---

## Scheduler

Implemented using:

```python
threading.Timer()
```

to automate CDC operations.

---

# Quick Review

## CDC Components

```text
Change Detection
Change Capture
Change Propagation
```

---

## Databases Requiring Initialization

```text
MySQL
Cassandra
```

---

## Databases Not Requiring Initialization

```text
MongoDB
Redis
```

---

## Python Libraries Used

```python
os
sys
time
threading
pymysql
pymongo
redis
cassandra-driver
```

---

## MySQL Table Used

```text
posts
```

---

## Cassandra Keyspace

```text
stamps
```

---

## Scheduler Component

```text
scheduler.py
```

---

## Source of Truth

```text
MySQL
```

---

## Final CDC Pipeline

```text
MySQL
   │
   ├── MongoDB
   ├── Redis
   └── Cassandra
```