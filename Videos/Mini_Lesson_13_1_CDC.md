# Mini-Lesson 13.1: Change Data Capture (CDC)

## What Is Change Data Capture (CDC)?

Change Data Capture (CDC) refers to techniques used to identify, track, and process changes made to a database.

CDC is important because data changes frequently in modern systems. As records are added, modified, or removed, downstream systems must remain synchronized.

CDC helps organizations:

- Detect database changes quickly
- Synchronize data efficiently
- Reduce processing time
- Reduce infrastructure costs
- Improve application performance

Common changes tracked by CDC include:

- INSERT
- UPDATE
- DELETE

---

# CDC Implementation Methods

There are multiple ways to implement CDC depending on system requirements.

This lesson focuses on two common approaches:

1. Audit Columns
2. Table Deltas

---

# Method 1: Audit Columns

Audit columns are one of the most common CDC techniques.

The idea is to track when records were created and modified by storing timestamps directly in the table.

## Example

Original table:

| Customer_ID | Created_Time |
|------------|-------------|
| 1 | 2021-03-13 |
| 2 | 2021-05-07 |
| 3 | 2021-10-24 |

A new column is added:

| Customer_ID | Created_Time | Changed_Time |
|------------|-------------|-------------|
| 1 | 2021-03-13 | 2021-10-31 |
| 2 | 2021-05-07 | NULL |
| 3 | 2021-10-24 | NULL |

The CDC process can use these timestamps to determine which records were added or modified.

---

## Audit Column Implementation Steps

### Step 1

Add a column called:

```text
Changed_Time
```

to the source table.

---

### Step 2

Determine the maximum values of:

```text
Created_Time
Changed_Time
```

in the target table.

---

### Step 3

Identify newly created records.

Example logic:

```sql
SELECT *
FROM source_table
WHERE Created_Time > max_created_time;
```

---

### Step 4

Identify modified records.

Example logic:

```sql
SELECT *
FROM source_table
WHERE Changed_Time > max_changed_time;
```

---

### Step 5

Apply changes to the destination table.

Actions may include:

- Insert new rows
- Update existing rows

---

## Advantages of Audit Columns

### Easy to Implement

Simple SQL queries can identify modifications.

### Minimal Additional Infrastructure

No additional CDC platform is required.

### Easy to Understand

Developers can easily inspect timestamps.

---

## Disadvantages of Audit Columns

### Risk of Errors

If timestamps are not maintained correctly, data inconsistencies may occur.

### Application Dependency

Developers must ensure timestamps are updated correctly.

### Limited Historical Tracking

Only the latest modification time is typically retained.

---

# Method 2: Table Deltas

Table deltas compare snapshots of data to determine what changed.

This technique identifies differences between:

- Previous snapshot
- Current snapshot

---

## Original Table

| Customer_ID | Last_Purchase |
|------------|--------------|
| 1 | 03-13-2021 |
| 2 | 05-07-2021 |
| 3 | 10-24-2021 |

---

## Changes Occur

Customer 1 makes a new purchase:

```text
10-31-2021
```

Customer 4 is added:

```text
11-02-2021
```

---

## Updated Table

| Customer_ID | Last_Purchase |
|------------|--------------|
| 1 | 10-31-2021 |
| 2 | 05-07-2021 |
| 3 | 10-24-2021 |
| 4 | 11-02-2021 |

---

## How Table Deltas Work

The CDC process compares:

```text
Previous Snapshot
```

against

```text
Current Snapshot
```

and identifies:

- New rows
- Modified rows
- Deleted rows

---

## Advantages of Table Deltas

### Accurate Change Detection

Changes can be identified precisely.

### Simple Queries

Comparisons are often straightforward.

### Good Data Integrity

Provides a reliable view of what changed.

---

## Disadvantages of Table Deltas

### Increased Storage Requirements

Three copies of data may be needed:

```text
Original Data
Previous Snapshot
Current Snapshot
```

### Higher Memory Usage

Additional storage and processing resources are required.

### More Expensive at Scale

Large datasets increase snapshot storage costs.

---

# Audit Columns vs Table Deltas

| Feature | Audit Columns | Table Deltas |
|----------|----------|----------|
| Implementation | Easy | Easy |
| Storage Usage | Low | High |
| Memory Usage | Low | High |
| Change Accuracy | Moderate | High |
| Timestamp Dependency | Yes | No |
| Historical Comparison | Limited | Strong |

---

# Relation to Module 13

The CDC pipeline built in Module 13 uses a simplified CDC approach.

The source database will be:

```text
MySQL
```

Changes will be propagated to:

```text
MongoDB
Redis
Cassandra
```

using periodic queries and time loops.

The concepts learned in this lesson explain how CDC systems determine which records need to be synchronized.

---

# Key Takeaways

- CDC identifies database changes efficiently.
- Audit columns use timestamps to detect modified records.
- Table deltas compare snapshots to identify differences.
- Audit columns require less storage but can introduce inconsistencies.
- Table deltas provide accurate change tracking but require more storage.
- CDC reduces synchronization costs by processing only changed records.