# updating data
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="kbtu",
    user="adil_zhapar",
    password="Adil2002")

cur = conn.cursor()

sql = '''
    UPDATE users 
    SET age = %s 
    ,registration_date = %s
    ,information = %s
    ,password = %s
    WHERE username = %s RETURNING *
'''

username = 'Adil'
user_age = 18
user_date = '13.08.2002'
user_info = 'Don\'t quote me, boy'
user_pass = 'Eazy-E'


cur.execute(sql, (user_age, user_date, user_info, user_pass, username))


final = cur.fetchall()
print(final)

cur.close()
conn.commit()
conn.close()
