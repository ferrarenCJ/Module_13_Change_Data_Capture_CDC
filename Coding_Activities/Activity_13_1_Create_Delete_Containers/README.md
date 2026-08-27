# Activity 13.1: Creating and Deleting Containers Using Python

## Overview

This activity demonstrates how to automate Docker container management using Python. Instead of manually creating and deleting containers through the command line, Python is used to execute Docker commands programmatically.

The activity focuses on creating and removing database containers that will be used later in Module 13 to implement Change Data Capture (CDC) workflows.

---

## Learning Outcome

Create and delete containers using Python.

---

## Technologies Used

- Python 3.11.9
- Docker Desktop
- Docker Engine
- Visual Studio Code
- OS Library (`os`)
- System Library (`sys`)

---

## Databases Used

The following database containers are created and managed:

| Database | Container Name | Host Port |
|-----------|-----------|-----------|
| MySQL | module13_mysql | 3307 |
| MongoDB | module13_mongodb | 27018 |
| Redis | module13_redis | 6380 |
| Cassandra | module13_cassandra | 9043 |

---

## Files

### Source Code

```text
containers.py
```

Python program that creates and deletes Docker containers.

### Documentation

```text
README.md
notes.md
```

### Screenshots

```text
screenshots/
```

Contains all screenshots required for submission.

---

## Creating Containers

Run the following command:

```bash
python containers.py --create
```

The script creates:

```text
module13_mysql
module13_mongodb
module13_redis
module13_cassandra
```

---

## Deleting Containers

Run the following command:

```bash
python containers.py --delete
```

The script:

1. Stops the containers.
2. Removes the containers.
3. Displays confirmation messages.

---

## Key Python Concepts

### Execute Shell Commands

```python
os.system()
```

Used to execute Docker commands from Python.

### Read Command-Line Arguments

```python
sys.argv
```

Used to determine whether the user wants to create or delete containers.

### Functions

```python
create_container()
delete_container()
```

Reusable functions used to manage container lifecycle operations.

---

## Docker Commands Used

### Create Container

```bash
docker run
```

### Stop Container

```bash
docker stop
```

### Remove Container

```bash
docker rm
```

### Verify Running Containers

```bash
docker ps
```

---

## Results

Successfully automated:

- MySQL container creation
- MongoDB container creation
- Redis container creation
- Cassandra container creation
- Container deletion and cleanup

The solution eliminates the need to manually execute multiple Docker commands and reduces the likelihood of configuration errors.

---

## Screenshots Included

1. container.py source code
2. Create MySQL container execution
3. MySQL container running in Docker Desktop
4. Delete MySQL container execution
5. MySQL container removed
6. Multi-database container creation code
7. Create all containers execution
8. Four containers running in Docker Desktop
9. Multi-database container deletion code
10. Delete all containers execution
11. All containers removed from Docker Desktop

---

## Key Takeaways

- Python can automate Docker container management.
- The `os` library can execute operating system commands.
- Docker commands can be embedded inside Python programs.
- Multiple database containers can be created from a single script.
- Automation reduces setup time and improves consistency.
- Container automation provides a foundation for implementing CDC pipelines in later module activities.