import os
import sys
import pymysql


def delete(container):

    cmd = f"docker stop {container}"

    result = os.system(cmd)

    if result == 0:

        cmd = f"docker rm {container}"

        os.system(cmd)

        print(f"Removed {container}")


def create(cmd, db):

    result = os.system(cmd)

    if result == 0:

        print(f"Created {db}")


def init_mysql():

    cnx = pymysql.connect(
        user="root",
        password="MyNewPass",
        host="127.0.0.1",
        port=5600
    )

    cursor = cnx.cursor()

    cursor.execute(
        "DROP DATABASE IF EXISTS pluto"
    )

    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS pluto"
    )

    cursor.execute(
        "USE pluto"
    )

    cursor.execute("""
        CREATE TABLE posts(
            id VARCHAR(36),
            stamp VARCHAR(20)
        )
    """)

    cnx.commit()

    print(
        "MySQL database initialized successfully."
    )

    cursor.close()
    cnx.close()


argument = ""

if len(sys.argv) > 1:

    argument = sys.argv[1]


if argument == "-delete":

    delete("final_mysql_container")
    delete("final_mongo_container")
    delete("final_redis_container")
    delete("final_cassandra_container")

    sys.exit()


if argument == "-create":

    create(
        "docker run "
        "-p 5600:3306 "
        "--name final_mysql_container "
        "-e MYSQL_ROOT_PASSWORD=MyNewPass "
        "-d mysql",
        "mysql"
    )

    create(
        "docker run "
        "-p 1800:27017 "
        "--name final_mongo_container "
        "-d mongo",
        "mongo"
    )

    create(
        "docker run "
        "-p 2400:6379 "
        "--name final_redis_container "
        "-d redis",
        "redis"
    )

    create(
        "docker run "
        "-p 1000:9042 "
        "--name final_cassandra_container "
        "-d cassandra",
        "cassandra"
    )

    sys.exit()


if argument == "-init":

    init_mysql()

    sys.exit()