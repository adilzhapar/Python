# inserting data
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="kbtu",
    user="adil_zhapar",
    password="Adil2002")

cur = conn.cursor()

sql = '''
    INSERT INTO users VALUES (%s, %s, %s, %s, %s) RETURNING *
'''

username = 'Jack'
user_age = 70
user_date = '21.04.2021'
user_info = 'Old man, take a look at my life'
user_pass = '1950'

cur.execute(sql, (username, user_age, user_date, user_info, user_pass))

final = cur.fetchall()
print(final)

cur.close()
conn.commit()
conn.close()
