import csv
import sqlite3
from abc import ABC, abstractmethod
from sqlite3 import Error
import os
# pip install psycopg2
import psycopg2


class DataClient(ABC):
    @abstractmethod
    def get_connection(self):
        pass

    @abstractmethod
    def create_mebel_table(self, conn):
        pass

    @abstractmethod
    def get_items(self, conn, price_from=0, price_to=100000):
        pass

    @abstractmethod
    def insert(self, conn, link, price, description):
        pass

    def run_test(self):
        conn = self.get_connection()
        self.create_mebel_table(conn)
        items = self.get_items(conn, price_from=10, price_to=30)
        for item in items:
            print(item)
        conn.close()


class CsvClient(DataClient):
    FILE_NAME = os.path.join(os.path.dirname(__file__), "mebel.csv")

    def get_connection(self):
        # Возвращаем None, так как в данном случае нет подключения к базе данных
        return None

    def create_mebel_table(self, conn):
        # Не нужно создавать таблицу, так как данные хранятся в CSV файле
        pass

    def get_items(self, conn, price_from=0, price_to=100000):
        items = []
        with open(self.FILE_NAME, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                price = int(row['price'])
                if price_from <= price <= price_to:
                    items.append(row)
        return items

    def insert(self, conn, link, price, description):
        with open(self.FILE_NAME, 'a', newline='') as csvfile:
            fieldnames = ['link', 'price', 'description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'link': link, 'price': price, 'description': description})


class PostgresClient(DataClient):
    USER = "postgres"
    PASSWORD = "postgres"
    HOST = "localhost"
    PORT = "5432"

    def get_connection(self):
        try:
            connection = psycopg2.connect(
                user=self.USER,
                password=self.PASSWORD,
                host=self.HOST,
                port=self.PORT
            )
            return connection
        except Error:
            print(Error)

    def create_mebel_table(self, conn):
        cursor_object = conn.cursor()
        cursor_object.execute(
            """
                CREATE TABLE IF NOT EXISTS mebel
                (
                    id serial PRIMARY KEY, 
                    link text, 
                    price integer, 
                    description text
                )
            """
        )
        conn.commit()

    def get_items(self, conn, price_from=0, price_to=100000):
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM mebel WHERE price >= {price_from} and price <= {price_to}')
        return cursor.fetchall()

    def insert(self, conn, link, price, description):
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO mebel (link, price, description) VALUES ('{link}', '{price}', '{description}')")
        conn.commit()


class Sqlite3Client(DataClient):
    DB_NAME = "kufar.db"

    def get_connection(self):
        try:
            conn = sqlite3.connect(self.DB_NAME)
            return conn
        except Error:
            print(Error)

    def create_mebel_table(self, conn):
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

    def get_items(self, conn, price_from=0, price_to=100000):
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM mebel WHERE price >= {price_from} and price <= {price_to}')
        return cursor.fetchall()

    def insert(self, conn, link, price, description):
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO mebel (link, price, description) VALUES ('{link}', '{price}', '{description}')")
        conn.commit()


data_client = CsvClient()
data_client.run_test()

data_client = PostgresClient()
data_client.run_test()

data_client = Sqlite3Client()
data_client.run_test()
