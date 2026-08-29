import os
import sys


def create():

    cmd = (
        "docker run "
        "-p 1000:9042 "
        "--name final_cassandra_container "
        "-d cassandra"
    )

    result = os.system(cmd)

    if result == 0:

        print(
            "Cassandra container created."
        )

if len(sys.argv) > 1:

    if sys.argv[1] == "create":

        create()