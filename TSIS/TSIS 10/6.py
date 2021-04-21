# deleting data
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="kbtu",
    user="adil_zhapar",
    password="Adil2002")

cur = conn.cursor()

sql = 'DELETE FROM users WHERE password = %s'
cur.execute(sql, ('1234',))


cur.close()
conn.commit()
conn.close()
