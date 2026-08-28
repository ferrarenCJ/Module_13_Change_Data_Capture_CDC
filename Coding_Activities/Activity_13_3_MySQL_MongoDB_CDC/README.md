# Activity 13.3: Performing CDC and Initializing MySQL and MongoDB Containers

## Objective

Build a simple Change Data Capture (CDC) pipeline using:

- MySQL
- MongoDB
- Python
- Docker

## Components

### container.py

Creates, initializes, and removes Docker containers.

### mysqldb.py

Reads, writes, and deletes data from MySQL.

### mongodb.py

Reads, writes, and deletes data from MongoDB.

### scheduler.py

Controls CDC processing using timers.

## CDC Workflow

MySQL
↓
Read Changes
↓
MongoDB
↓
Verify Results

## Commands

### Create Containers

```bash
python container.py -create
```

### Initialize Database

```bash
python container.py -init
```

### Run Scheduler

```bash
python scheduler.py
```

### Delete Containers

```bash
python container.py -delete
```

## Database

### MySQL

Database:

```text
pluto
```

Table:

```text
posts
```

Columns:

```text
id
stamp
```

### MongoDB

Database:

```text
pluto
```

Collection:

```text
posts
```

## Key Takeaways

- Initialized a MySQL database programmatically.
- Connected to MongoDB using Python.
- Implemented basic CDC from MySQL to MongoDB.
- Used timers to simulate periodic database activity.
- Automated container lifecycle management using Python and Docker.