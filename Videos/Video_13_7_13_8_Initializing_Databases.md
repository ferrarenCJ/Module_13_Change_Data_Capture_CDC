# Module 13 - Videos 13.7 & 13.8 Notes
# Initializing Databases Using CDC

## Overview

This section introduces two important concepts required to build a CDC pipeline:

1. Database Initialization
2. Time Loops

Before changes can be propagated between databases, the destination databases must first be initialized and prepared to receive data.

Time loops are then used to periodically check for changes and execute CDC operations automatically.

---

# Video 13.7: Initializing Databases

## What is Database Initialization?

Database initialization is the process of preparing a database for use.

This may include:

- Creating databases
- Creating tables
- Defining relationships
- Creating indexes
- Creating schemas
- Loading initial data

Database initialization is frequently automated when containers are created.

---

## Why Initialization is Necessary

Consider a newly created MySQL container.

Initially:

```text
MySQL Container
```

may contain:

```text
No application database
No custom tables
No user data
```

Before CDC can occur, the required database structures must exist.

---

## Example Relational Database Initialization

### Create Database

```sql
CREATE DATABASE cdc_db;
```

---

### Create Table

```sql
CREATE TABLE customers (
    customer_id INT,
    customer_name VARCHAR(100)
);
```

---

### Create Relationships

```sql
CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    FOREIGN KEY(customer_id)
        REFERENCES customers(customer_id)
);
```

---

## Automating Initialization

Instead of manually executing initialization commands:

```text
Create Container
Connect to Database
Run CREATE TABLE
Run INSERT
Repeat
```

Python can automate initialization.

Workflow:

```text
Python
   │
   ▼

Docker Container
   │
   ▼

Database Initialization
   │
   ▼

Ready for CDC
```

---

## Why Initialization Matters for CDC

CDC relies on target systems that are already configured.

Example:

```text
Source:
MySQL

Target:
MongoDB
Redis
Cassandra
```

These systems must exist before changes can be propagated.

---

## Benefits of Automated Initialization

### Consistency

Every deployment uses identical configuration.

### Speed

Provisioning occurs automatically.

### Reliability

Fewer manual setup errors.

### Reproducibility

Identical environments can be recreated repeatedly.

---

# Video 13.8: Time Loops

## What is a Time Loop?

A time loop executes a function repeatedly at fixed intervals.

Instead of running a process once:

```text
Execute
Stop
```

a time loop continuously executes tasks.

```text
Execute
Wait
Execute
Wait
Execute
Wait
```

---

## Why Time Loops are Important

CDC systems need to continually monitor source databases.

Example:

```text
Detect Change
Capture Change
Propagate Change
Repeat
```

Time loops provide this automation.

---

## Python Time Module

Python provides timing functions through:

```python
import time
```

---

## Basic Example

```python
import time

while True:

    print("Checking for changes...")

    time.sleep(5)
```

Output:

```text
Checking for changes...

(wait 5 seconds)

Checking for changes...

(wait 5 seconds)
```

---

## How a Time Loop Works

```text
Start
  │
  ▼

Run Function
  │
  ▼

Wait
  │
  ▼

Run Function Again
  │
  ▼

Wait
  │
  ▼

Repeat
```

---

## Simulating Database Changes

The instructor demonstrates using a timer program to periodically execute a user-defined function.

Example:

```python
def update_database():

    print(
        "Database updated"
    )


while True:

    update_database()

    time.sleep(10)
```

---

## CDC and Time Loops

A CDC process typically follows:

```text
Query Source Database
     │
     ▼

Identify Changes
     │
     ▼

Propagate Changes
     │
     ▼

Sleep
     │
     ▼

Repeat
```

The loop runs continuously while the application is active.

---

## Example CDC Loop

```python
while True:

    detect_changes()

    propagate_changes()

    time.sleep(5)
```

---

## Advantages of Time Loops

### Automation

No manual intervention required.

### Continuous Monitoring

Changes are detected repeatedly.

### Near Real-Time Synchronization

Updates occur at regular intervals.

### Simplicity

Easy to implement and understand.

---

## Limitations

### Polling Delay

Changes are detected only at the next interval.

Example:

```text
Loop Interval = 30 Seconds
```

Change may wait up to 30 seconds before detection.

### Resource Usage

Very short intervals can increase CPU and database usage.

---

# Relationship to Module 13

Upcoming coding activities will use:

## Containers

```text
MySQL
MongoDB
Redis
Cassandra
```

---

## Database Initialization

Preparing each database.

---

## Time Loops

Repeated execution of CDC logic.

---

## Change Data Capture

Synchronizing changes across databases.

---

# Key Concepts

## Database Initialization

Preparing a database for application use.

Common tasks:

- Create database
- Create table
- Create relationships

---

## Time Loop

Repeated execution of a function.

Example:

```python
while True:
```

---

## Delay Execution

```python
time.sleep()
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

## What is database initialization?

```text
Preparing a database by creating databases,
tables, schemas, and relationships.
```

---

## Why initialize databases?

```text
So they are ready to receive data
and support CDC operations.
```

---

## Which Python module is used for timing?

```text
time
```

---

## What does time.sleep() do?

```text
Pauses execution for a specified period.
```

---

## Why are time loops useful in CDC?

```text
They allow changes to be detected and
propagated periodically.
```

---

# Key Takeaways

- Databases often require initialization before use.
- Initialization can be automated with Python.
- CDC systems depend on properly initialized databases.
- Time loops enable periodic execution of functions.
- CDC commonly uses time loops to monitor for changes.
- The combination of containers, initialization, and time loops forms the basis of the CDC pipeline built later in Module 13.