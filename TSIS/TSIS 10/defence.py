import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="kbtu",
    user="adil_zhapar",
    password="Adil2002")

cur = conn.cursor()

sql = """
        UPDATE users SET information=%s WHERE username='KBTU'
    """

user_name = "KBTU"
user_age = 20
registr = '01-09-2020'
info = 'Good day!'
password = 'defence'

cur.execute(sql, (info, ))

conn.commit()
cur.close()
conn.close()