# CDC Concepts Cheat Sheet

## Change Data Capture (CDC)

CDC is a process that identifies, captures, and propagates changes made to a source database.

Types of changes:

```text
INSERT
UPDATE
DELETE
```

---

# CDC Components

## Change Detection

Identify that a change occurred.

Examples:

```text
New row inserted
Row updated
Row deleted
```

---

## Change Capture

Capture information about the change.

Examples:

```text
Primary Key
Timestamp
Changed Values
Operation Type
```

---

## Change Propagation

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

# CDC Methods

## Audit Columns

Examples:

```text
created_date
updated_date
modified_timestamp
```

Example Query:

```sql
SELECT *
FROM posts
WHERE updated_date > last_sync;
```

---

## Periodic Queries

Run repeatedly using polling.

Example:

```sql
SELECT *
FROM orders
WHERE stamp > last_run;
```

---

## Database Triggers

Execute automatically on:

```text
INSERT
UPDATE
DELETE
```

---

## Dual Writes

Application writes to multiple databases.