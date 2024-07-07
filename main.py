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

def change_client(id, field, new_field):
    with psycopg2.connect(database='HW_db', user='postgres', password='LSamovar69') as conn:
        with conn.cursor() as cur:
            query = f'UPDATE clients SET {field} = %s WHERE id = %s;'
            cur.execute(query, (new_field, id))
            

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

def find_client(search="%"):
    with psycopg2.connect(database='HW_db', user='postgres', password='LSamovar69') as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT * 
                        FROM clients
                        WHERE first_name LIKE %s OR last_name LIKE %s OR email LIKE %s;
                        """, (f'%{search}%',f'%{search}%',f'%{search}%'))
            result = cur.fetchone()
            return result
        
def all_client():
    with psycopg2.connect(database='HW_db', user='postgres', password='LSamovar69') as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT * FROM clients;""")
            result = cur.fetchall()
            return result


if __name__ == "__main__":
    create_db = createdb()
    phone_table = create_phone_table()
    add_client = add_new_client('name', 'surname', 'email')
    phone = add_phone(1, '1234567890')
    change = change_client(7,'first_name', 'name')
    del_phone = delete_client_phone(1, '1234567890')
    del_client = delete_client_by_id(1)
    find = find_client('Vadim')
    print(find)
    all = all_client()
    print(all)