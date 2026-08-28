# MongoDB Commands Cheat Sheet

## Connect

```bash
docker exec -it some-mongo mongosh
```

---

## Show Databases

```javascript
show dbs
```

---

## Use Database

```javascript
use pluto
```

---

## Show Collections

```javascript
show collections
```

---

## Find Documents

```javascript
db.posts.find()
```

---

## Find One Document

```javascript
db.posts.findOne()
```

---

## Sort Descending

```javascript
db.posts.find().sort(
    { stamp: -1 }
)
```

---

## Limit Results

```javascript
db.posts.find()
        .limit(5)
```

---

## Count Documents

```javascript
db.posts.countDocuments()
```

---

## Insert Document

```javascript
db.posts.insertOne({
    stamp: "2026-08-28"
})
```

---

## Delete Documents

```javascript
db.posts.deleteMany({})
```

---

# Python Connection

```python
from pymongo import MongoClient

client = MongoClient(
    "mongodb://localhost:27017"
)

db = client.pluto

posts = db.posts
```