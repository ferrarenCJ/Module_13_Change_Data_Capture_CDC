# Cassandra Commands Cheat Sheet

## Access Cassandra

```bash
docker exec -it some-cassandra cqlsh
```

---

## Show Keyspaces

```sql
DESCRIBE KEYSPACES;
```

---

## Use Keyspace

```sql
USE stamps;
```

---

## Show Tables

```sql
DESCRIBE TABLES;
```

---

## Create Keyspace

```sql
CREATE KEYSPACE stamps
WITH REPLICATION =
{
    'class':'SimpleStrategy',
    'replication_factor':1
};
```

---

## Create Table

```sql
CREATE TABLE posts (
    id text PRIMARY KEY,
    stamp text
);
```

---

## View Table Data

```sql
SELECT *
FROM posts;
```

---

## Insert Row

```sql
INSERT INTO posts
(id, stamp)
VALUES
(
    'maxTimeStamp',
    '2026-08-28'
);
```

---

## Update Row

```sql
UPDATE posts
SET stamp='2026-08-28'
WHERE id='maxTimeStamp';
```

---

## Delete Row

```sql
DELETE
FROM posts
WHERE id='maxTimeStamp';
```

---

# Python Connection

```python
from cassandra.cluster import Cluster

cluster = Cluster(
    ['localhost'],
    port=9042
)

session = cluster.connect(
    'stamps'
)
```

---

## Execute Query

```python
session.execute(
    "SELECT * FROM posts"
)
```