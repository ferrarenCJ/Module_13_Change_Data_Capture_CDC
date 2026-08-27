# Self-Study Knowledge Check 13.1
# Change Data Capture (CDC)

## Score

Completed Successfully

Questions: 5

Correct Answers: 5/5

---

## Question 1

### What does CDC stand for?

✅ Correct Answer:

```text
Change Data Capture
```

### Notes

CDC is a software process used to identify and track changes made to data within a database.

Changes typically include:

- INSERT
- UPDATE
- DELETE

---

## Question 2

### What are the components of CDC?

✅ Correct Answer:

```text
Change Detection
Change Capture
Change Propagation
```

### Notes

#### Change Detection

Determines that a change occurred.

#### Change Capture

Records details about the change.

#### Change Propagation

Transfers the change to downstream systems.

---

## Question 3

### What are some disadvantages of using the database trigger CDC method?

✅ Correct Answer:

```text
All of these answers are correct.
```

### Notes

Potential disadvantages include:

- Database performance impact
- Increased storage requirements
- Backup complications
- Trigger failures may affect transactions
- Additional maintenance complexity

---

## Question 4

### Which CDC method leverages timestamps?

✅ Correct Answer:

```text
Periodic Queries
```

### Notes

Periodic query CDC uses timestamp columns such as:

```text
created_time
updated_time
changed_time
```

Example:

```sql
SELECT *
FROM customers
WHERE updated_time > last_processed_time;
```

---

## Question 5

### What is a common disadvantage of using audit columns such as updated_time?

✅ Correct Answer:

```text
It is easy to make errors that can cause inconsistencies in your data.
```

### Notes

Advantages:

- Simple implementation
- Easy SQL queries

Disadvantages:

- Timestamp maintenance errors
- Missed updates
- Data inconsistencies

---

# Key Concepts Learned

## CDC

Change Data Capture identifies and propagates data changes.

### Operations Tracked

- INSERT
- UPDATE
- DELETE

### Core CDC Components

1. Change Detection
2. Change Capture
3. Change Propagation

### Common CDC Methods

#### Audit Columns

Uses:

```text
created_time
updated_time
changed_time
```

Pros:

- Easy implementation

Cons:

- Potential data inconsistencies

#### Database Triggers

Pros:

- Near real-time tracking

Cons:

- Performance overhead
- Increased storage requirements

#### Periodic Queries

Pros:

- Simple implementation
- Timestamp-based tracking

Cons:

- Not truly real-time

#### Table Deltas

Pros:

- Accurate change detection

Cons:

- Requires additional storage

---

# Exam Tips

Remember:

### CDC Components

```text
Detect
Capture
Propagate
```

### CDC Operations

```text
INSERT
UPDATE
DELETE
```

### Timestamp-Based CDC

```text
Periodic Queries
```

### Audit Column Disadvantage

```text
Data inconsistencies
```

### Trigger Disadvantages

```text
Performance impact
Storage overhead
Transaction failures
```
