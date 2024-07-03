
import psycopg2

conn = psycopg2.connect(database='HW_db', user='postgres', password='LSamovar69')

def createdb(conn):
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS clients (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                phone VARCHAR(255)
                );""")
    cur.close()
    conn.commit()
    return conn.close()

def add_new_client(conn, first_name, last_name, email, phone=None):
    cur = conn.cursor()
    cur.execute("""INSERT INTO clients(first_name, last_name, email, phone)
                 VALUES (%s, %s, %s, %s);
                """, (first_name, last_name, email, phone))
    cur.close()
    conn.commit()
    return conn.close()

def add_phone(conn, id, phone):
    cur = conn.cursor()
    cur.execute(""" INSERT INTO clients(phone) VALUES (%s)
                WHERE id =%s ;
                """, (phone, id, ))
    cur.close()
    conn.commit()
    return conn.close()

def change_client(conn, id, first_name, last_name, email, phone):
    cur = conn.cursor()
    cur.execute("""UPDATE clients SET first_name=%s, last_name=%s, email=%s, phone=%s
                 WHERE id=%s;
                """, (first_name, last_name, email, phone, id))
    cur.close()
    conn.commit()
    return conn.close()

def delete_client_phone(conn, id, phone):
    cur = conn.cursor()
    cur.execute("""DELETE FROM clients
                 WHERE id=%s AND phone=%s;
                """, (id, phone))
    cur.close()
    conn.commit()
    return conn.close()

def delete_client_by_id(conn, id):
    cur = conn.cursor()
    cur.execute("""DELETE FROM clients
                 WHERE id=%s;
                """, (id,))
    cur.close()
    conn.commit()
    return conn.close()

def find_client(conn, first_name, last_name, email, phone):
    cur = conn.cursor()
    cur.execute("""SELECT * FROM clients
                 WHERE first_name=%s AND last_name=%s AND email=%s AND phone=%s;
                """, (first_name, last_name, email, phone))
    result = cur.fetchone()
    cur.close()
    return result

with psycopg2.connect(database=None, user=None, password=None) as conn:
    createdb(conn)
    add_new_client(conn, 'Vadim', 'Levchenko', 'Levchenkovadim2001@mail.ru')
    add_phone(conn, 1, '+1234567890')
    change_client(conn, 1, 'Vadim', 'Levcenko', 'Levchenkovadim2001@mail.ru', '+9876543210')
    delete_client_phone(conn, 1, '+1234567890')
    delete_client_by_id(conn, 1)
    find_client(conn, 'Vadim', 'Levchenko', 'Levchenkovadim2001@mail.ru', '+9876543210')
    