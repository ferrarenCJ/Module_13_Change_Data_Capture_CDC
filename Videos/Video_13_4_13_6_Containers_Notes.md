# Module 13 - Videos 13.4-13.6 Notes
# Containers in Python

## Overview

This section introduces how Python can automate operating system tasks and Docker container management by executing shell commands.

Topics include:

- Running shell commands from Python
- Creating Docker containers programmatically
- Deleting Docker containers programmatically
- Automating database container management
- Preparing containers for CDC workflows

---

# Video 13.4: Embedding Terminal Window Commands in Python

## Purpose

Python can execute operating system commands directly from a program.

This allows automation of tasks such as:

- Creating containers
- Deleting containers
- Initializing databases
- Clearing databases
- Listing files
- Running Docker commands

---

## The os Module

The video demonstrates the use of:

```python
import os
```

The `os` module provides access to operating system functionality.

Example:

```python
os.system("dir")
```

on Windows.

Example:

```python
os.system("ls -l")
```

on Linux/macOS.

---

## Cross-Platform Compatibility

Python can determine the operating system by checking:

```python
os.name
```

### Windows

```python
os.name == "nt"
```

### Linux/macOS

```python
os.name != "nt"
```

---

## Executing Shell Commands

Example:

```python
result = os.system("dir")
```

The command runs in the system shell.

The return value indicates success or failure.

```python
print(result)
```

---

## Command-Line Arguments

The video also demonstrates:

```python
import sys
```

Using:

```python
sys.argv
```

allows users to pass arguments to a Python script.

Example:

```python
python shell.py --list
```

Retrieving the argument:

```python
argument = sys.argv[1]
```

---

## Example Workflow

```text
User runs script
        │
        ▼

Python receives argument
        │
        ▼

Python executes shell command
        │
        ▼

Operating System performs action
```

---

## Key Takeaway

Python can act as an automation layer for operating system and Docker commands.

---

# Video 13.5: Creating Containers Using Python

## Goal

Automate Docker container creation.

Instead of manually typing:

```bash
docker run
```

a Python script can execute the command automatically.

---

## Traditional Docker Method

Example:

```bash
docker run hello-world
```

or

```bash
docker run -d --name mysql-server mysql
```

---

## Python Automation

Example:

```python
import os

os.system(
    "docker run hello-world"
)
```

Python sends the Docker command directly to the operating system.

---

## Why Automate Container Creation?

Benefits include:

### Repeatability

The same environment can be rebuilt repeatedly.

### Consistency

All users receive the same configuration.

### Scalability

Multiple containers can be provisioned automatically.
