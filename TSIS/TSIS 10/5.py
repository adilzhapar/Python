# data query
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="kbtu",
    user="adil_zhapar",
    password="Adil2002")

cur = conn.cursor()

sql = 'SELECT username, age, information FROM users ORDER BY username'
cur.execute(sql)

results = cur.fetchall()
print(results)

cur.close()

conn.close()
