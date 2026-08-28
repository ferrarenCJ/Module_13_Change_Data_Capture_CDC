from cassandra.cluster import Cluster

keyspace = 'stamps'

cluster = Cluster(
    ['localhost'],
    port=9042
)

session = cluster.connect(keyspace)


def write(stamps):

    session.execute(
        """
        UPDATE posts
        SET stamp = %s
        WHERE id = %s
        IF EXISTS
        """,
        (
            str(stamps[0]),
            "maxTimeStamp"
        )
    )


def read():

    result = session.execute(
        "select stamp from posts where id = %s",
        ("maxTimeStamp",)
    )

    row = result.one()

    if row:
        return row.stamp

    return None


def delete():

    session.execute(
        "delete from posts where id = %s",
        ("maxTimeStamp",)
    )