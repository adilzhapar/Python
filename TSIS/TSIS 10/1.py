# Connecting to DB
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="kbtu",
    user="adil_zhapar",
    password="Adil2002")

cur = conn.cursor()

print('PostgreSQL database version:')
cur.execute('SELECT version()')

db_version = cur.fetchone()
print(db_version)

cur.close()