import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database='kbtu',
    user='adil_zhapar',
    password='Adil2002'
)

cur = conn.cursor()

sql = """INSERT INTO cars VALUES (%s, %s, %s, %s)"""

car_id = 1
car_name = 'BMW'
car_model = 'e39'
release_date = '13-01-1998'

cur.execute(sql, (car_id, car_name, car_model, release_date))

conn.commit()
cur.close()
conn.close()