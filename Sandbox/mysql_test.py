import pymysql

try:

    cnx = pymysql.connect(
        user='root',
        password='MyNewPass',
        host='127.0.0.1',
        db='pluto'
    )

    cursor = cnx.cursor()

    cursor.execute("SELECT COUNT(*) FROM posts")

    count = cursor.fetchone()[0]

    print(f"MySQL connection successful.")
    print(f"Posts count: {count}")

    cursor.close()
    cnx.close()

except Exception as e:

    print(f"MySQL Error: {e}")