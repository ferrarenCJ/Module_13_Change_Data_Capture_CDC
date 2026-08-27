import os
import sys


def container_exists(container_name):

    if os.name == "nt":
        cmd = (
            f"docker inspect {container_name} "
            f"> nul 2>&1"
        )
    else:
        cmd = (
            f"docker inspect {container_name} "
            f"> /dev/null 2>&1"
        )

    result = os.system(cmd)

    return result == 0


def create_container(command, database, container_name):

    if container_exists(container_name):

        print(
            f"{database} container already exists."
        )

        return

    result = os.system(command)

    if result == 0:

        print(
            f"{database} container created successfully."
        )

    else:

        print(
            f"Error creating {database} container."
        )


def delete_container(container_name):

    if not container_exists(container_name):

        print(
            f"{container_name} does not exist."
        )

        return

    os.system(
        f"docker stop {container_name}"
    )

    result = os.system(
        f"docker rm {container_name}"
    )

    if result == 0:

        print(
            f"{container_name} deleted successfully."
        )

    else:

        print(
            f"Error deleting {container_name}."
        )


argument = ""

if len(sys.argv) > 1:
    argument = sys.argv[1]


if argument == "--create":

    print("\nCreating containers...\n")

    create_container(
        "docker run -d "
        "--name module13_mysql "
        "-e MYSQL_ROOT_PASSWORD=password "
        "-p 3307:3306 mysql",
        "MySQL",
        "module13_mysql"
    )

    create_container(
        "docker run -d "
        "--name module13_mongodb "
        "-p 27018:27017 mongo",
        "MongoDB",
        "module13_mongodb"
    )

    create_container(
        "docker run -d "
        "--name module13_redis "
        "-p 6380:6379 redis",
        "Redis",
        "module13_redis"
    )

    create_container(
        "docker run -d "
        "--name module13_cassandra "
        "-p 9043:9042 cassandra",
        "Cassandra",
        "module13_cassandra"
    )

    print("\nContainer creation complete.")


elif argument == "--delete":

    print("\nDeleting containers...\n")

    delete_container(
        "module13_mysql"
    )

    delete_container(
        "module13_mongodb"
    )

    delete_container(
        "module13_redis"
    )

    delete_container(
        "module13_cassandra"
    )

    print("\nContainer deletion complete.")


else:

    print("\nUsage:")
    print("python containers.py --create")
    print("python containers.py --delete")