import redis

try:

    client = redis.Redis(
        host='localhost',
        port=6379,
        db=0
    )

    value = client.get(
        "LastInsertDate"
    )

    print("Redis connection successful.")

    if value:
        print(
            f"LastInsertDate = "
            f"{value.decode('utf-8')}"
        )
    else:
        print(
            "LastInsertDate not found."
        )

except Exception as e:

    print(f"Redis Error: {e}")