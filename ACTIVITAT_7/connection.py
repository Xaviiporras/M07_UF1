import psycopg2 as pg

conn = pg.connect(
    database="postgres",
    user='user_postgres',
    password='pass_postgres',
    host='localhost',
    port='5432'
)

connection = conn.cursor()

print(connection)