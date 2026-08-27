# Mini-Lesson 13.3: Time Loops

## Overview

Time loops and timers are commonly used to schedule tasks that should execute after a specified amount of time or at regular intervals.

In Change Data Capture (CDC) systems, timers can be used to periodically check for database changes and propagate updates to downstream systems.

This lesson focuses on Python's built-in `Timer` class from the `threading` module.

---

# What is a Timer?

A timer is a mechanism that schedules a function to execute after a specified delay.

Timers are useful when:

- Delaying execution of a task
- Sending notifications
- Performing retries
- Executing background processes
- Simulating periodic database updates

Unlike loops, a timer executes a function only once unless another timer is created.

---

# Python Timer Class

Python provides the `Timer` class through the `threading` module.

Import the module:

```python
import threading
```

---

# General Syntax

```python
threading.Timer(
    interval,
    your_function
)
```

Where:

| Parameter | Description |
|------------|-------------|
| interval | Number of seconds to wait |
| your_function | Function to execute after the delay |

---

# Example: Execute a Function After Five Seconds

```python
import threading


def pcde():

    print(
        "This is a course in data engineering."
    )


timer = threading.Timer(
    5.0,
    pcde
)

timer.start()

print("Exit")
```

---

# Expected Output

```text
Exit

(wait 5 seconds)

This is a course in data engineering.
```

---

# How It Works

### Step 1

Python creates a timer.

```python
timer = threading.Timer(...)
```

---

### Step 2

The timer is started.

```python
timer.start()
```

---

### Step 3

The program immediately continues.

```python
print("Exit")
```

---

### Step 4

Five seconds later:

```python
pcde()
```

executes automatically.

---

# Visualization

```text
Start Program
      │
      ▼

Create Timer
      │
      ▼

Start Timer
      │
      ▼

Program Continues
      │
      ▼

Timer Expires
      │
      ▼

Execute Function
```

---

# Cancelling a Timer

A timer can be cancelled before it executes.

This only works if the timer is still waiting.

---

# Syntax

```python
timer.cancel()
```

---

# Example

```python
import threading


def pcde():

    print(
        "This is a course in data engineering."
    )


timer = threading.Timer(
    5.0,
    pcde
)

timer.start()

print(
    "Cancelling timer"
)

timer.cancel()

print("Exit")
```

---

# Output

```text
Cancelling timer

Exit
```

Notice that:

```text
This is a course in data engineering.
```

never appears because the timer was cancelled before it executed.

---

# Timer Lifecycle

```text
Timer Created
      │
      ▼

Timer Started
      │
      ▼

Waiting
      │
      ├────────► Cancelled
      │
      ▼

Execute Function
```

---

# Timer vs Loop

## Timer

Executes once.

Example:

```python
threading.Timer(
    5,
    my_function
)
```

Behavior:

```text
Wait 5 seconds
Execute once
Stop
```

---

## Loop

Executes repeatedly.

Example:

```python
while True:

    my_function()
```

Behavior:

```text
Execute
Repeat
Execute
Repeat
Execute
Repeat
```

---

# Why This Matters for CDC

CDC systems need to periodically:

```text
Check Source Database
Identify Changes
Propagate Updates
```

Timers and loops provide a mechanism for scheduling these operations.

Example:

```text
MySQL
   │
   ▼

Detect Changes
   │
   ▼

MongoDB
Redis
Cassandra
```

A timer can trigger a CDC function after a delay.

A loop can continuously repeat CDC operations.

---

# Example CDC Timer

```python
import threading


def perform_cdc():

    print(
        "Checking for changes..."
    )


timer = threading.Timer(
    10,
    perform_cdc
)

timer.start()
```

Expected behavior:

```text
Wait 10 seconds

Checking for changes...
```

---

# Example Continuous CDC Loop

```python
import time


while True:

    print(
        "Checking for changes..."
    )

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

# Applications of Time Loops

## Change Data Capture

Monitor databases for changes.

---

## Monitoring Systems

Check application health.

---

## Notification Systems

Send delayed messages or alerts.

---

## Retry Logic

Retry failed API calls.

---

## Database Synchronization

Keep multiple databases synchronized.

---

# Advantages

### Automation

Tasks run without manual intervention.

### Reliability

Operations occur on schedule.

### Reusability

Functions can be scheduled repeatedly.

### Simplicity

Easy to implement.

---

# Limitations

### Delayed Execution

A timer executes only after the specified interval.

### Not Continuous

Timers are one-time events unless restarted.

### Resource Usage

Very short intervals can increase resource consumption.

---

# Key Concepts

## Import Timer Module

```python
import threading
```

---

## Create Timer

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

## Continuous Loop

```python
while True:
```

---

# Knowledge Check Preparation

## Which module contains the Timer class?

```text
threading
```

---

## What does Timer do?

```text
Schedules a function to run
after a specified delay.
```

---

## How many times does a Timer execute?

```text
Once
```

---

## How do you start a Timer?

```python
timer.start()
```

---

## How do you cancel a Timer?

```python
timer.cancel()
```

---

## What structure continuously repeats execution?

```python
while True:
```

---

# Key Takeaways

- Python's `threading.Timer` schedules a function after a delay.
- A timer executes once unless restarted.
- Timers can be cancelled before execution.
- Time loops are useful for recurring tasks.
- CDC systems often use timing mechanisms to monitor and propagate database changes.
- Timers and loops form the foundation for the next activity: Implementing Time Loops.