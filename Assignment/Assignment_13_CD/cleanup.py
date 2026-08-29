import os
import sys


containers = [
    "final_mysql_container",
    "final_mongo_container",
    "final_redis_container",
    "final_cassandra_container"
]


def delete(container):

    os.system(
        f"docker stop {container}"
    )

    os.system(
        f"docker rm {container}"
    )

    print(
        f"Removed {container}"
    )


if len(sys.argv) > 1:

    if sys.argv[1] == "delete":

        for container in containers:

            delete(container)
