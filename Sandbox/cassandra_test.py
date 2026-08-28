from cassandra.cluster import Cluster

try:

    cluster = Cluster(
        ['localhost'],
        port=9042
    )

    session = cluster.connect(
        'stamps'
    )

    result = session.execute(
        """
        SELECT *
        FROM posts
        """
    )

    print(
        "Cassandra connection successful."
    )

    for row in result:
        print(row)

except Exception as e:

    print(f"Cassandra Error: {e}")