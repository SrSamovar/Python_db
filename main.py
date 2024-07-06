import psycopg2


def createdb():
    with psycopg2.connect(database='HW_db', user='postgres', password='LSamovar69') as conn:
        with conn.cursor() as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS clients(
                        id SERIAL PRIMARY KEY,
                        first_name VARCHAR(255),
                        last_name VARCHAR(255),
                        email VARCHAR(255) UNIQUE
                        );""")
            

def create_phone_table():
    with psycopg2.connect(database='HW_db', user='postgres', password='LSamovar69') as conn:
        with conn.cursor() as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS phones (
                        id SERIAL,
                        clients_id INTEGER NOT NULL REFERENCES clients(id),
                        phone VARCHAR(30) UNIQUE NOT NULL
                        );""")

def add_new_client(first_name, last_name, email):
    with psycopg2.connect(database='HW_db', user='postgres', password='LSamovar69') as conn:
        with conn.cursor() as cur: 
            cur.execute("""INSERT INTO clients(first_name, last_name, email)
                        VALUES (%s, %s, %s);
                        """, (first_name, last_name, email))

def add_phone(clients_id, phone):
    with psycopg2.connect(database='HW_db', user='postgres', password='LSamovar69') as conn:
        with conn.cursor() as cur:
            cur.execute("""INSERT INTO phones(clients_id, phone)
                        VALUES (%s, %s);
                        """, (clients_id, phone))

def change_client(id, first_name=None, last_name=None, email=None):
    with psycopg2.connect(database='HW_db', user='postgres', password='LSamovar69') as conn:
        with conn.cursor() as cur:
            cur.execute("""UPDATE clients SET first_name=%s, last_name=%s, email=%s
                        WHERE id=%s;
                        """, (first_name, last_name, email, id))

def delete_client_phone(id, phone):
    with psycopg2.connect(database='HW_db', user='postgres', password='LSamovar69') as conn:
        with conn.cursor() as cur:
            cur.execute("""DELETE FROM phones
                        WHERE id=%s AND phone=%s;
                        """, (id, phone))

def delete_client_by_id(id):
    with psycopg2.connect(database='HW_db', user='postgres', password='LSamovar69') as conn:
        with conn.cursor() as cur:
            cur.execute("""DELETE FROM clients
                        WHERE id=%s;
                        """, (id,))

def find_client(first_name=None, last_name=None, email=None):
    with psycopg2.connect(database='HW_db', user='postgres', password='LSamovar69') as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT * 
                        FROM clients
                        WHERE first_name=%s OR last_name=%s OR email=%s;
                        """, (first_name, last_name, email))
            result = cur.fetchone()
            return result


if __name__ == "__main__":
    create_db = createdb()
    phone_table = create_phone_table()
    add_client = add_new_client('name', 'surname', 'email')
    phone = add_phone(1, '1234567890')
    change = change_client(1,'new_name')
    del_phone = delete_client_phone(1, '1234567890')
    del_client = delete_client_by_id(1)
    find = find_client('name')
    print(find)