import psycopg2
from config import config

def create_tables():
    commands = (
        '''
        CREATE TABLE cars (
            car_id serial PRIMARY KEY,
            car_name VARCHAR ( 50 ) NOT NULL,
            car_model VARCHAR ( 10 ) NOT NULL,
            release_date DATE
        );
        ''',
        """
        CREATE TABLE cars_roles (
            car_id INT NOT NULL,
            grant_date TIMESTAMP,
            PRIMARY KEY (car_id),
            FOREIGN KEY (car_id)
                REFERENCES cars (car_id)
        );
        """,
    )
    conn = None
    try: 
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except Exception as e:
        print(str(e))
    if conn is not None:
        conn.close()

create_tables()