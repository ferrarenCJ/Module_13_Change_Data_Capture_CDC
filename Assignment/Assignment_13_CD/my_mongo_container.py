import os
import sys

def create():

    cmd = (
        "docker run "
        "-p 1800:27017 "
        "--name final_mongo_container "
        "-d mongo"
    )

    result = os.system(cmd)

    if result == 0:

        print(
            "MongoDB container created."
        )

if len(sys.argv) > 1:

    if sys.argv[1] == "create":

        create()