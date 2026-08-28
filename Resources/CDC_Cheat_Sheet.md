# Change Data Capture (CDC) Cheat Sheet

## What is CDC?

Change Data Capture (CDC) is a process used to identify, capture, and propagate changes made to a source database.

Common changes tracked:

```text
INSERT
UPDATE
DELETE
```

---

# CDC Components

## 1. Change Detection

Detect that a change occurred.

Example:

```text
New customer added
Work order updated
Record deleted
```

---

## 2. Change Capture

Capture details of the change.

Example:

```text
Record ID
Timestamp
Operation Type
Changed Values
```

---

## 3. Change Propagation

Send changes to downstream systems.

Example:

```text
MySQL
   │
   ▼
MongoDB

Redis

Cassandra
```

---

# CDC Workflow

```text
Detect
   │
   ▼
Capture
   │
   ▼
Propagate
```

Remember:

```text