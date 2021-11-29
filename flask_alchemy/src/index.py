import psycopg2
import psycopg2.extras

DB_HOST = "localhost"
DB_NAME = "veterinaria"
DB_USER = "postgres"
DB_PASS = ""

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
s = "SELECT * FROM estado"
cur.execute(s) # Execute the SQL
list_users = cur.fetchall()

print(list_users)

# cur.execute("insert into estado(description) values (%s)", ['durmiendo'])
# conn.commit()
# cur.execute(s)