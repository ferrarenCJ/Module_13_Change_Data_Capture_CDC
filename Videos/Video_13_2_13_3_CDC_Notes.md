# Module 13 - Videos 13.2 & 13.3 Notes
# Introduction to Change Data Capture (CDC)

## Video 13.2: Change Data Capture (CDC) Overview

### Overview

As systems grow in size and complexity, organizations often need a single source of truth for their data while maintaining copies of that data in other systems optimized for specific workloads such as analytics, caching, reporting, or search.

Change Data Capture (CDC) is a process that keeps these systems synchronized by detecting and propagating changes made to the source database.

Rather than copying all data repeatedly, CDC propagates only the records that have changed.

---

## What is Change Data Capture (CDC)?

Change Data Capture (CDC) is a technique used to identify, capture, and propagate modifications made to a database.

CDC tracks three primary database operations:

- INSERT
- UPDATE
- DELETE

Whenever one of these operations occurs, the CDC process identifies the change and distributes it to downstream systems.

---

## Source of Truth and Derived Data

### Source of Truth

The source of truth is the authoritative system where data is originally stored and maintained.

Example:

```text
MySQL Database
```

This database contains the official version of the data.

---

### Derived Data

Derived data consists of copies or transformations of the source data stored in other systems.

Examples:

```text
MongoDB
Redis
Cassandra
```

These systems may support:

- Reporting
- Analytics
- Search
- Caching
- High-performance querying

---

## Why CDC is Important

Without CDC, organizations typically perform:

- Full database reloads
- Large batch processes
- Manual synchronizations

These approaches become increasingly expensive and inefficient as data volume grows.

CDC solves this problem by synchronizing only the records that have changed.

---

## Benefits of CDC

### Reduced Data Movement

Instead of transferring an entire database, CDC transfers only changed records.

### Faster Synchronization

Target systems receive updates quickly after changes occur.

### Better Scalability

CDC works well in systems containing large amounts of data.

### Lower Resource Usage

CDC reduces:

- Network traffic
- CPU utilization
- Storage operations

---

## Three Core Components of CDC

### 1. Change Detection

Change detection identifies when a database modification occurs.

Examples include:

```sql
INSERT INTO customers VALUES (...);
```

```sql
UPDATE customers
SET status = 'ACTIVE'
WHERE customer_id = 101;
```

```sql
DELETE FROM customers
WHERE customer_id = 101;
```

The system first determines that a change has occurred.

---

### 2. Change Capture

After detecting the change, the CDC process records information describing what changed.

Example:

```json
{
  "operation": "UPDATE",
  "table": "customers",
  "record_id": 101
}
```

This metadata can then be transmitted to downstream systems.

---

### 3. Change Propagation

Once captured, the change is applied to target systems.

Example:

```text
MySQL
   ↓
MongoDB
```

or

```text
MySQL
   ↓
Redis
```

or

```text
MySQL
   ↓
Cassandra
```

The goal is to ensure all systems remain synchronized.

---

## CDC Workflow

```text
Source Database
       │
       ▼
Change Detection
       │
       ▼
Change Capture
       │
       ▼
Change Propagation
       │
       ▼
Target Systems
```

---

## Key Takeaways from Video 13.2

- CDC tracks INSERT, UPDATE, and DELETE operations.
- CDC synchronizes source and target systems.
- CDC reduces data movement and processing overhead.
- CDC consists of three primary stages:
  - Change Detection
  - Change Capture
  - Change Propagation

---

# Video 13.3: Basics of a CDC System

## Overview

In this module, a complete CDC pipeline will be constructed using a MySQL database as the source of truth.

Changes made to MySQL will be propagated to:

- MongoDB
- Redis
- Cassandra

using a periodic query-based CDC approach.

---

## Source Database

The source system for the CDC pipeline is:

```text
MySQL
```

The MySQL database serves as the authoritative source of data.

---

## Target Databases

The CDC pipeline propagates data to three target systems:

### MongoDB

Document-oriented NoSQL database.

### Redis

In-memory key-value database commonly used for caching and high-speed data access.

### Cassandra

Distributed NoSQL database optimized for scalability and availability.

---

## CDC Architecture

```text
                 Source Database

                      MySQL
                         │
                         ▼

                 Change Detection
                         │
                         ▼

                  Change Capture
                         │
                         ▼

                Change Propagation
                         │
       ┌─────────────────┼─────────────────┐
       │                 │                 │
       ▼                 ▼                 ▼

    MongoDB           Redis          Cassandra
```

---

## Periodic Query Approach

The CDC system implemented in this module uses a periodic query model.

Instead of reading transaction logs or using database triggers, the system periodically checks the source database for updates.

Conceptually:

```python
while True:
    check_for_changes()
```

The CDC process repeatedly:

1. Queries MySQL
2. Detects changes
3. Captures change information
4. Propagates changes
5. Repeats the process

---

## Why Use Periodic Queries?

Advantages include:

- Simplicity
- Easy implementation
- Easy debugging
- Suitable for learning CDC concepts

Although production systems may use transaction logs or event streams, periodic queries provide an effective educational implementation.

---

## Example CDC Flow

### Step 1

A record is inserted into MySQL:

```sql
INSERT INTO users VALUES (...);
```

---

### Step 2

The CDC process detects the newly inserted row.

---

### Step 3

The new data is captured.

---

### Step 4

The data is propagated.

```text
MongoDB ← Updated

Redis ← Updated

Cassandra ← Updated
```

---

## Technologies Used Throughout Module 13

### Python

Used to:

- Automate container creation
- Implement CDC logic
- Schedule tasks

### Docker

Used to create and manage database containers.

### MySQL

Acts as the source of truth.

### MongoDB

Stores propagated document data.

### Redis

Stores propagated key-value data.

### Cassandra

Stores propagated distributed data.

### Time Loops

Used to periodically execute CDC logic.

Example:

```python
while True:
    perform_cdc()
```

---

## Key Takeaways from Video 13.3

- MySQL serves as the source database.
- MongoDB, Redis, and Cassandra act as target databases.
- Changes flow from MySQL to downstream databases.
- The module implements CDC using a periodic query approach.
- Time loops will repeatedly execute CDC operations.
- Docker containers will host all databases.

---

# Module 13 CDC Architecture Summary

```text
                     Source of Truth

                           MySQL
                              │
                              ▼

                     Detect Changes
                              │
                              ▼

                     Capture Changes
                              │
                              ▼

                    Propagate Changes
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
         ▼                    ▼                    ▼

      MongoDB             Redis             Cassandra
```

---

# Knowledge Check Preparation

## What are the three CDC components?

1. Change Detection
2. Change Capture
3. Change Propagation

---

## Which operations does CDC monitor?

- INSERT
- UPDATE
- DELETE

---

## What is the source of truth in this module?

```text
MySQL
```

---

## Which databases receive propagated changes?

```text
MongoDB
Redis
Cassandra
```

---

## What CDC approach is implemented in this module?

```text
Periodic Query Approach
```

---

# Key Concepts to Remember

- CDC keeps multiple databases synchronized.
- Source systems provide authoritative data.
- Target systems contain derived data.
- CDC improves efficiency by propagating only changed records.
- The CDC pipeline for this module is:

```text
MySQL → MongoDB → Redis → Cassandra
```

- Time loops are used to execute CDC processes repeatedly.