import subprocess

tests = [
    "mysql_test.py",
    "mongodb_test.py",
    "redis_test.py",
    "cassandra_test.py"
]

for test in tests:

    print("\n" + "=" * 50)
    print(f"Running {test}")
    print("=" * 50)

    subprocess.run(
        ["python", test]
    )