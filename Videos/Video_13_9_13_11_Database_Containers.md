# Module 13 - Videos 13.9 & 13.10 Notes
# Initializing Database Containers

## Overview

These videos begin the implementation of a complete Change Data Capture (CDC) pipeline.

The CDC architecture introduced in this section consists of:

```text
MySQL
   │
   ▼

CDC Process
   │
   ▼

MongoDB
```

MySQL acts as the source of truth, while MongoDB receives propagated changes.

The videos demonstrate:

- Initializing a MySQL database using Python
- Creating tables and loading data
- Connecting to MongoDB
- Writing data to MongoDB
- Scheduling database operations using timers

---

# Video 13.9
# CDC – Creating a Database Using Python and MySQL

## Goal

Programmatically initialize a MySQL database running inside a Docker container.

---

## Why Initialization is Required

A newly created MySQL container contains only the database engine.

Before CDC can occur, you must create:

- Database
- Tables
- Relationships
- Initial Data

For example:

```sql
CREATE DATABASE books;
```

```sql
CREATE TABLE books (
    id INT,
    title VARCHAR(100)
);
```

---

## MySQL as the Source of Truth

In the CDC architecture:

```text
MySQL
```

serves as the authoritative source database.

All changes originate here.

Examples:

```text
INSERT
UPDATE
DELETE
```

The CDC process identifies these changes and distributes them to downstream systems.

---

## Python and MySQL

Python can connect directly to MySQL using:

```python
import mysql.connector
```

Typical workflow:

```text
Connect
   │
   ▼

Create Database
   │
   ▼

Create Tables
   │
   ▼

Insert Data
   │
   ▼

Commit Changes
```

---

## General Workflow

```text
Python Script
      │
      ▼

MySQL Container
      │
      ▼

Create Database
      │
      ▼

Create Tables
      │
      ▼

Insert Records
      │
      ▼

Ready for CDC
```

---

## Importance to CDC

CDC requires an initialized source database.

Without:

```text
Database
Tables
Data
```

there is nothing to monitor.

---

# Video 13.10
# Connecting and Writing to a Database Using MongoDB

## Goal

Programmatically connect to MongoDB and store data propagated from MySQL.

---

## MongoDB Initialization

MongoDB requires less setup than relational databases.

Unlike MySQL:

```text
No CREATE DATABASE required
No CREATE TABLE required
```

MongoDB automatically creates databases and collections when data is inserted.

---

## MongoDB Workflow

```text
Connect
   │
   ▼

Select Database
   │
   ▼

Select Collection
   │
   ▼

Insert Documents
```

---

## MongoDB as a CDC Target

In this module:

```text
MySQL
```

is the source.

```text
MongoDB
```

is the destination.

When changes occur in MySQL:

```text
Detect
Capture
Propagate
```

data is written into MongoDB.

---

## Example Document Structure

```json
{
  "title": "Harry Potter",
  "pages": 250,
  "author": {
    "first": "J.K.",
    "last": "Rowling"
  }
}
```

---

## Python and MongoDB

Typical library:

```python
from pymongo import MongoClient
```

General workflow:

```python
client = MongoClient()

db = client.books

collection = db.titles

collection.insert_one(document)
```

---

# Scheduler

## Why a Scheduler is Needed

CDC is not a one-time operation.

The process must periodically:

```text
Check Source Database
Identify Changes
Propagate Changes
```

The scheduler automates this process.

---

## Scheduler Using Timers

The video demonstrates using:

```python
threading.Timer()
```

to repeatedly perform database operations.

---

## Conceptual Workflow

```text
Timer Starts
      │
      ▼

Read MySQL
      │
      ▼

Detect Changes
      │
      ▼

Write MongoDB
      │
      ▼

Restart Timer
      │
      ▼

Repeat
```

---

# Simulating Database Activity

The scheduler can be used to:

### Simulate Inserts

```text
Add new records
```

### Simulate Updates

```text
Modify records
```

### Simulate CDC Events

```text
Detect changes
```

### Test Synchronization

```text
Validate data propagation
```

---

# CDC Architecture

```text
                  Source Database

                       MySQL
                          │
                          ▼

                    CDC Process
                          │
                          ▼

                     MongoDB
```

Later activities will extend this architecture to:

```text
Redis
Cassandra
```

---

# Key Concepts

## MySQL

Requires initialization.

Example:

```sql
CREATE DATABASE
CREATE TABLE
INSERT
```

---

## MongoDB

No explicit initialization required.

Database and collections are created automatically.

---

## Scheduler

Automates repeated database activity.

---

## Timer

```python
threading.Timer()
```

---

## CDC Workflow

```text
Detect
Capture
Propagate
Repeat
```

---

# Knowledge Check Preparation

## Which database acts as the source of truth?

```text
MySQL
```

---

## Which database receives propagated changes?

```text
MongoDB
```

---

## Which database requires initialization?

```text
MySQL
```

---

## Which database automatically creates collections?

```text
MongoDB
```

---

## Why is a scheduler used?

```text
To periodically check for changes
and propagate updates.
```

---

# Key Takeaways

- MySQL serves as the source database in the CDC pipeline.
- MySQL must be initialized before CDC can occur.
- MongoDB acts as a target system that receives propagated changes.
- MongoDB requires less setup than relational databases.
- Python can automate database initialization and data loading.
- Timers and schedulers allow CDC operations to run periodically.
- These videos lay the foundation for Coding Activities 13.3 through 13.5.