# Mini-Lesson 13.2: Containers in Python

## Overview

Managing Docker containers manually is acceptable for small projects, but it becomes inefficient when working with multiple databases or repeatedly creating and deleting containers.

Python can automate container management by executing Docker commands through the operating system.

Benefits include:

- Faster deployment
- Fewer manual errors
- Consistent environments
- Easier automation
- Repeatable testing workflows

---

# Why Use Python for Container Management?

Without automation:

```bash
docker run ...
docker run ...
docker run ...
docker run ...
```

must be executed manually every time.

As the number of containers increases, manual setup becomes:

- Time-consuming
- Error-prone
- Difficult to maintain

Python solves this problem by automating Docker commands.

---

# Required Python Modules

The examples use:

```python
import os
import sys
```

## os

Provides access to operating system commands.

Example:

```python
os.system("docker ps")
```

---

## sys

Reads command-line arguments.

Example:

```python
sys.argv
```

---

# Creating Containers

The lesson demonstrates using a Python function to execute Docker commands.

## Create Function

```python
def create(cmd, db):

    result = os.system(cmd)

    if result == 0:

        print(
            f"Created {db}"
        )
```

---

## Example MySQL Container

```python
create(
    "docker run "
    "-p 3306:3306 "
    "--name some-mysql "
    "-e MYSQL_ROOT_PASSWORD=MyNewPass "
    "-d mysql",
    "mysql"
)
```

Equivalent Docker command:

```bash
docker run \
-p 3306:3306 \
--name some-mysql \
-e MYSQL_ROOT_PASSWORD=MyNewPass \
-d mysql
```

---

# Container Creation Workflow

```text
Python Program
      │
      ▼

Read Argument
      │
      ▼

Execute Docker Command
      │
      ▼

Create Container
      │
      ▼

Display Success Message
```

---

# Database Containers Used in Module 13

## MySQL

```bash
docker run \
-p 3306:3306 \
--name some-mysql \
-e MYSQL_ROOT_PASSWORD=MyNewPass \
-d mysql
```

---

## MongoDB

```bash
docker run \
-p 27017:27017 \
--name some-mongo \
-d mongo
```

---

## Redis

```bash
docker run \
-p 6379:6379 \
--name some-redis \
-d redis
```

---

## Cassandra

```bash
docker run \
-p 9042:9042 \
--name some-cassandra \
-d cassandra
```

---

# Creating Multiple Containers

The lesson encourages creating all database containers from a single script.

Example:

```text
Python Script
      │
      ├─ MySQL
      ├─ MongoDB
      ├─ Redis
      └─ Cassandra
```

This is exactly what we implemented in:

```text
Sandbox/containers.py
```

using:

```text
module13_mysql
module13_mongodb
module13_redis
module13_cassandra
```

---

# Deleting Containers

A delete function can automate cleanup.

## Delete Function

```python
def delete(container):

    cmd = f"docker stop {container}"

    result = os.system(cmd)

    if result == 0:

        cmd = f"docker rm {container}"

        result = os.system(cmd)

        print(
            f"Removed {container}"
        )
```

---

# Example

```python
delete("some-mysql")
```

Equivalent commands:

```bash
docker stop some-mysql

docker rm some-mysql
```

---

# Container Deletion Workflow

```text
Python Program
      │
      ▼

Stop Container
      │
      ▼

Remove Container
      │
      ▼

Display Success Message
```

---

# Command Line Arguments

## Create

```bash
python containers.py -create
```

---

## Delete

```bash
python containers.py -delete
```

The script evaluates:

```python
sys.argv[1]
```

and executes the appropriate action.

---

# Module 13 Implementation

For Module 13 we built:

## Create

```bash
python containers.py --create
```

Creates:

```text
module13_mysql
module13_mongodb
module13_redis
module13_cassandra
```

---

## Delete

```bash
python containers.py --delete
```

Deletes:

```text
module13_mysql
module13_mongodb
module13_redis
module13_cassandra
```

---

# Key Concepts

## Python Modules

```python
import os
import sys
```

---

## Execute Shell Commands

```python
os.system()
```

---

## Read Arguments

```python
sys.argv
```

---

## Create Docker Container

```bash
docker run
```

---

## Stop Docker Container

```bash
docker stop
```

---

## Remove Docker Container

```bash
docker rm
```

---

# Advantages of Container Automation

### Speed

Multiple containers can be created simultaneously.

### Consistency

Every deployment uses the same configuration.

### Reduced Errors

Removes manual typing mistakes.

### Scalability

Supports larger environments.

### Reusability

Scripts can be executed repeatedly.

---

# Key Takeaways

- Python can automate Docker commands using the `os` module.
- Command-line arguments can be processed through `sys.argv`.
- Docker containers can be created with `docker run`.
- Containers can be deleted with `docker stop` and `docker rm`.
- Automation reduces setup time and configuration errors.
- Multiple database containers can be deployed from a single Python script.