# Activity 13.5: Performing CDC and Initializing a Cassandra Database Container

## Objective

Extend the CDC pipeline by adding Cassandra.

## Final CDC Architecture

MySQL
↓
MongoDB
↓
Redis
↓
Cassandra

## Components

- container.py
- mysqldb.py
- mongodb.py
- redisdb.py
- cassandradb.py
- scheduler.py

## Cassandra

Keyspace:

stamps

Table:

posts

Primary Key:

id

Tracking Record:

maxTimeStamp

## Commands

Create:

python container.py -create

Initialize:

python container.py -init

Run Scheduler:

python scheduler.py

Delete:

python container.py -delete

## Key Takeaways

- Cassandra requires initialization.
- Cassandra stores the most recent MySQL timestamp.
- CDC now propagates data to MongoDB, Redis, and Cassandra.
- MySQL remains the source of truth.