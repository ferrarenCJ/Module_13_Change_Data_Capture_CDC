import pymysql
import uuid
from datetime import datetime

cnx = pymysql.connect(
    user="root",
    password="MyNewPass",
    host="127.0.0.1",
    port=5600,
    db="pluto"
)

cursor = cnx.cursor()


def write():

    id = str(uuid.uuid4())

    stamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    query = (
        f'INSERT INTO posts '
        f'VALUES("{id}","{stamp}")'
    )

    cursor.execute(query)

    cnx.commit()


def read():

    cursor.execute(
        """
        SELECT *
        FROM posts
        ORDER BY stamp DESC
        LIMIT 5
        """
    )

    return cursor.fetchall()


write()

print(
    "Data inserted into MySQL."
)