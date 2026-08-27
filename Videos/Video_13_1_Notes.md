# Module 13 - Video 13.1 Notes
## Introduction to Change Data Capture (CDC)

### Overview

Module 13 introduces Change Data Capture (CDC), a technique used to identify and propagate changes made in a database. CDC enables applications to react to database changes without repeatedly processing all records.

The module focuses on:

- Change Data Capture (CDC)
- Docker containers
- Container automation using Python
- Database initialization
- Time loops
- CDC implementation across multiple databases

---

## What is CDC?

Change Data Capture (CDC) is a process that tracks changes made to data and propagates those changes to other systems.

CDC monitors three primary operations:

- INSERT
- UPDATE
- DELETE

CDC also notifies downstream systems when changes occur.

---

## Three Components of CDC

### 1. Change Detection

Identifies that a database change has occurred.

Examples:

```sql
INSERT INTO customers VALUES (...);

UPDATE customers
SET status = 'ACTIVE'
WHERE customer_id = 100;

DELETE FROM customers
WHERE customer_id = 100;