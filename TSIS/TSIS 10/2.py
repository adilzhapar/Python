# Creating table
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="kbtu",
    user="adil_zhapar",
    password="Adil2002")

cur = conn.cursor()

cur.execute(
    '''CREATE TABLE users(
    username VARCHAR(255),
    age INTEGER,
    registration_date DATE,
    information TEXT,
    password VARCHAR(50)
    );
    '''
    )
cur.close()
conn.commit()
conn.close()
