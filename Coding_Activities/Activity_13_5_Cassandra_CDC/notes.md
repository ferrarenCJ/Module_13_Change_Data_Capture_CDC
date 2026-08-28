# Activity 13.5 Notes

## Learning Outcomes

- Initialize database containers
- Perform CDC across multiple databases
- Integrate Cassandra into an existing CDC pipeline
- Automate CDC using timer loops

---

## Activity Overview

This activity extends the CDC architecture from Activity 13.4 by adding Cassandra as an additional destination database.

Previous CDC Flow:

```text
MySQL
   │
   ▼
MongoDB
   │
   ▼
Redis
```

New CDC Flow:

```text
MySQL
   │
   ├── MongoDB
   │
   ├── Redis
   │
   └── Cassandra
```

MySQL remains the source of truth for all propagated data.

---

## Cassandra Container

### Create Cassandra Container

```python
create(
    'docker run -p 9042:9042 '
    '--name some-cassandra '
    '-d cassandra',
    'cassandra'
)
```

### Delete Cassandra Container

```python
delete('some-cassandra')
```

---

## Cassandra Initialization

Unlike MongoDB and Redis, Cassandra requires initialization.

### Keyspace

```text
stamps
```

### Table

```text
posts
```

### Schema

```sql
CREATE TABLE posts (
    id text PRIMARY KEY,
    stamp text
);
```

### Seed Record

```sql
insert into posts
(id, stamp)
values
(
    'maxTimeStamp',
    '1975-01-01 00:00:00'
)
IF NOT EXISTS
```

---

## init_cassandra()

```python
def init_cassandra():

    keyspace = None

    cluster = Cluster(
        ['localhost'],
        port=9042
    )

    session = cluster.connect(
 