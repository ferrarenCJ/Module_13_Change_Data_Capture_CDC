# Self-Study Discussion 13.1: Thinking Like a Data Scientist - CDC

One resource that I found particularly helpful during this module is the official Docker documentation. Since several activities required creating, initializing, and deleting database containers, the Docker command references helped me better understand how container port mappings, container names, and database images work.

Resource:

https://docs.docker.com/

Another useful resource was the PyMySQL documentation, which helped me understand how Python applications connect to MySQL databases and execute SQL statements programmatically.

Resource:

https://pymysql.readthedocs.io/

These resources were especially helpful when working through Activities 13.3 through 13.5. The module required creating a CDC pipeline that propagated data from MySQL to MongoDB, Redis, and Cassandra. Understanding how Docker containers communicate through mapped ports and how Python database drivers establish connections made troubleshooting much easier.

One tip I would share with classmates is to verify each database independently before running the scheduler. For example:

- Verify MySQL using `SHOW DATABASES` and `SHOW TABLES`
- Verify MongoDB using `mongosh` and `db.posts.find()`
- Verify Redis using `GET LastInsertDate`
- Verify Cassandra using `SELECT * FROM posts`

Testing each component separately helped me quickly identify issues with ports