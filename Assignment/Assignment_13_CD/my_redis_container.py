import os
import sys


def create():

    cmd = (
        "docker run "
        "-p 2400:6379 "
        "--name final_redis_container "
        "-d redis"
    )

    result = os.system(cmd)

    if result == 0:

        print(
            "Redis container created."
        )


if len(sys.argv) > 1:

    if sys.argv[1] == "create":

        create()