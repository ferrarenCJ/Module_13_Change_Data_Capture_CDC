import os


def delete(container):

    cmd = f"docker stop {container}"

    result = os.system(cmd)

    if result == 0:

        cmd = f"docker rm {container}"

        os.system(cmd)

        print(
            f"Removed {container}"
        )


delete("final_mysql_container")
delete("final_mongo_container")
delete("final_redis_container")
delete("final_cassandra_container")