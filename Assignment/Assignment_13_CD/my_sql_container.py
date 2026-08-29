import os
import sys

def create():
    cmd = (
        "docker run "
        "-p 5600:3306 "
        "--name final_mysql_container "
        "-e MYSQL_ROOT_PASSWORD=MyNewPass "
        "-d mysql"
    )

    result = os.system(cmd)

    if result == 0:
        print("MySQL container created.")


if len(sys.argv) > 1:

    if sys.argv[1] == "create":
        create()