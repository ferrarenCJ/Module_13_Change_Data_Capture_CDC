# Self-Study Knowledge Check 13.3
# Initializing Databases and Time Loops

## Score

Completed Successfully

Questions: 4

Correct Answers: 4/4

---

# Question 1

## Which of the following databases do not need to be initialized?

✅ Correct Answer

```text
MongoDB
```

### Notes

MongoDB is schema-flexible and automatically creates:

- Databases
- Collections

when data is inserted.

In contrast:

### MySQL

Requires initialization:

```sql
CREATE DATABASE
CREATE TABLE
```

### Cassandra

Requires initialization:

```sql
CREATE KEYSPACE
CREATE TABLE
```

---

# Question 2

## What is a time loop?

✅ Correct Answer

```text
When a function calls itself in a loop in a specific interval of time, it is called a time loop.
```

### Notes

Time loops repeatedly execute a function after a delay.

Example:

```python
import threading

def process():

    print("Running")

    threading.Timer(
        5,
        process
    ).start()

process()
```

Workflow:

```text
Run
 ↓
Wait
 ↓
Run
 ↓
Wait
 ↓
Repeat
```

---

# Question 3

## Which libraries are required to create a time loop in Python?

✅ Correct Answer

```text
threading
```

### Notes

The Timer class belongs to:

```python
import threading
```

Example:

```python
timer = threading.Timer(
    5,
    my_function
)
```

---

# Question 4

## What is the syntax to cancel a timer in Python?

✅ Correct Answer

```python
timer.cancel()
```

### Notes

Example:

```python
import threading

timer = threading.Timer(
    5,
    my_function
)

timer.start()

timer.cancel()
```

The scheduled function will not execute if the timer is cancelled before expiration.

---

# Key Concepts Learned

## Database Initialization

Preparing databases before use.

Examples:

### MySQL

```sql
CREATE DATABASE
CREATE TABLE
```

### Cassandra

```sql
CREATE KEYSPACE
CREATE TABLE
```

### MongoDB

No manual initialization required.

---

## Timer

Schedules a function to execute after a delay.

```python
threading.Timer()
```

---

## Start Timer

```python
timer.start()
```

---

## Cancel Timer

```python
timer.cancel()
```

---

## Time Loops

Functions repeatedly execute after fixed intervals.

Example:

```text
Run
Wait
Run
Wait
Repeat
```

---

# CDC Applications

Time loops can be used to:

- Periodically query MySQL
- Detect data changes
- Capture changes
- Propagate changes
- Synchronize MongoDB
- Synchronize Redis
- Synchronize Cassandra

Example CDC cycle:

```text
MySQL
   │
   ▼

Detect Changes
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

---

# Knowledge Check Summary

## MongoDB

```text
Does not require initialization.
```

## Time Loop

```text
A function repeatedly calling itself after a delay.
```

## Library

```text
threading
```

## Cancel Timer

```python
timer.cancel()
```

---

# Key Takeaways

- MongoDB typically does not require explicit initialization.
- MySQL and Cassandra require initialization.
- Python's `threading.Timer` is used for timer-based execution.
- `timer.cancel()` stops a timer before execution.
- Time loops are essential for CDC systems that periodically monitor databases for changes.