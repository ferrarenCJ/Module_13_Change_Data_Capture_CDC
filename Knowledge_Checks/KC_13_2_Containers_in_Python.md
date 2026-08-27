# Self-Study Knowledge Check 13.2
# Containers in Python

## Score

Completed Successfully

Questions: 6

Correct Answers: 6/6

---

# Question 1

## Which Python library is required to run shell commands through Python?

✅ Correct Answer

```text
os
```

### Notes

The `os` library allows Python programs to execute operating system and shell commands.

Example:

```python
import os

os.system("docker ps")
```

---

# Question 2

## How do you write and execute a shell command to list files in Python?

✅ Correct Answer

```python
cmd = f'ls -l'
result = os.system(cmd)
print(result)
```

### Notes

Steps:

1. Store shell command in a variable.
2. Execute command with `os.system()`.
3. Display result.

---

# Question 3

## Can you create a Docker container using Python?

✅ Correct Answer

```text
Yes
```

### Notes

Python can create containers by executing Docker commands.

Example:

```python
os.system(
    "docker run -d --name some-mysql mysql"
)
```

Supported containers include:

- MySQL
- MongoDB
- Redis
- Cassandra

---

# Question 4

## What syntax would you use to write the shell command to stop a container in Python?

✅ Correct Answer

```python
cmd = f'docker stop container_nm'
```

### Notes

Example:

```python
container_name = "module13_mysql"

cmd = f"docker stop {container_name}"

os.system(cmd)
```

---

# Question 5

## Can Python create multiple containers using different Docker images?

✅ Correct Answer

```text
Yes, you can write a Python program to create these containers using appropriate Docker images.
```

### Notes

A single Python script can create multiple containers.

Example:

```text
MySQL
MongoDB
Redis
Cassandra
```

This is exactly what was implemented using:

```text
module13_mysql
module13_mongodb
module13_redis
module13_cassandra
```

---

# Question 6

## What is the advantage of managing and creating containers using Python programs?

✅ Correct Answer

```text
To speed up container management and avoid errors
```

### Notes

Benefits:

- Faster deployment
- Reduced manual effort
- Greater consistency
- Fewer configuration mistakes
- Easier automation

---

# Key Concepts Learned

## Python Modules

### os

Used to execute shell commands.

Example:

```python
os.system()
```

### sys

Used to read command-line arguments.

Example:

```python
sys.argv
```

---

# Docker Commands

## Create Container

```bash
docker run
```

## Stop Container

```bash
docker stop
```

## Delete Container

```bash
docker rm
```

## List Containers

```bash
docker ps
```

---

# Container Automation Workflow

```text
Python
   │
   ▼

os.system()
   │
   ▼

Docker Command
   │
   ▼

Container Created/Deleted
```

---

# Practical Work Completed

Created a Python automation program:

```text
containers.py
```

that can:

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

# Key Takeaways

- Python can automate Docker operations.
- The `os` library is used to execute shell commands.
- Multiple containers can be managed through a single Python script.
- Automation improves speed and reduces errors.
- Container lifecycle management is a key skill required for CDC implementations.