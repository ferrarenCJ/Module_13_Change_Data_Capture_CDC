# Sandbox/environment_test.py

def check_import(module_name, import_stmt):
    try:
        exec(import_stmt)
        print(f"{module_name} OK")
    except Exception as ex:
        print(f"{module_name} FAILED: {ex}")

check_import("Docker SDK", "import docker")
check_import("PyMongo", "import pymongo")
check_import("Redis", "import redis")
check_import("MySQL Connector", "import mysql.connector")
check_import("Cassandra Driver", "from cassandra.cluster import Cluster")

print("\nEnvironment Ready")