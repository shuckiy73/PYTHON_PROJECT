import sqlite3
from sqlite3 import Error


def get_connection():
    try:
        conn = sqlite3.connect('kufar.db')
        return conn
    except Error:
        print(Error)


def create_mebel_table(conn):
    cursor_object = conn.cursor()
    cursor_object.execute(
        """
            CREATE TABLE IF NOT EXISTS mebel
            (
                id integer PRIMARY KEY autoincrement, 
                link text, 
                price integer, 
                description text
            )
        """
    )
    conn.commit()


def get_items(conn, price_from=0, price_to=100000):
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM mebel WHERE price >= {price_from} and price <= {price_to}')
    return cursor.fetchall()


def insert(conn, link, price, description):
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO mebel (link, price, description) VALUES ('{link}', '{price}', '{description}')")
    conn.commit()


def sqlite_test():
    conn = get_connection()
    create_mebel_table(conn)
    items = get_items(conn, 10, 30)
    for item in items:
        print(item)
    conn.close()


sqlite_test()
