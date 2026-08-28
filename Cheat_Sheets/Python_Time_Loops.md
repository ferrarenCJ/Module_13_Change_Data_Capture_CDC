# Python Time Loops Cheat Sheet

## Required Libraries

```python
import threading
import time
```

---

# Create Timer

```python
timer = threading.Timer(
    5,
    my_function
)
```

---

# Start Timer

```python
timer.start()
```

---

# Cancel Timer

```python
timer.cancel()
```

---

# Delay Execution

```python
time.sleep(3)
```

---

# One-Time Timer Example

```python
import threading

def hello():

    print("Hello")

timer = threading.Timer(
    5,
    hello
)

timer.start()
```

---

# Time Loop Example

```python
from threading import Timer

def timeloop():

    print("Running")

    Timer(
        5,
        timeloop
    ).start()

timeloop()
```

---

# CDC Scheduler Example

```python
def timeloop():

    mysql()

    mongo()

    redis()

    cassandra()

    verify()

    Timer(
        5,
        timeloop
    ).start()
```

---

# Useful Functions

## Current Time

```python
time.ctime()
```

---

## Current Timestamp

```python
datetime.now()
```

---

## Stop Program

```python
Ctrl + C
```

---

# Activity 13.2 Concepts

```python
zip()
```

```python
time.sleep()
```

```python
threading.Timer()
```

```python
timer.cancel()
```

---

# Module 13 Usage

Timers are used to:

- Schedule CDC operations
- Simulate inserts
- Simulate updates
- Poll source databases
- Verify synchronization