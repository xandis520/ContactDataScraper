# Blacklista: Tworzenie/dodawanie/usuwanie/sprawdzanie
# Company_data: Tworzenie/dodawanie/aktualizowanie


import pymysql


class SqlDataManager:
    def __init__(self, host='localhost', user='root', password='None', db='', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password="",
            database=db,
            charset=charset,
            cursorclass=cursorclass,
        )
        self.cursor = self.connection.cursor()

    def create_database(self, database_name):
        sql_statement = f"CREATE DATABASE IF NOT EXISTS {database_name};"
        self.cursor.execute(sql_statement)

    def delete_database(self, database_name):
        sql_statement = f"DROP DATABASE IF EXISTS {database_name};"
        self.cursor.execute(sql_statement)

    def create_table(self, database_name, table_name, columns):
        self.create_database(database_name)
        self.connection.select_db(database_name)
        sql_statement = f"CREATE TABLE IF NOT EXISTS {table_name}{columns};"
        self.cursor.execute(sql_statement)

    def delete_table(self, database_name, table_name):
        self.connection.select_db(database_name)
        sql_statement = f"DROP TABLE IF EXISTS {table_name};"
        self.cursor.execute(sql_statement)

    def add_columns(self, database_name, table_name, columns):
        self.connection.select_db(database_name)
        try:
            for column in columns:
                sql_statement = f"ALTER TABLE {table_name} ADD {column};"
                self.cursor.execute(sql_statement)
        except pymysql.err.ProgrammingError:
            raise pymysql.err.ProgrammingError(
                'You probably gave existing column name')

    def add_column(self, database_name, table_name, column):
        self.connection.select_db(database_name)
        try:
            sql_statement = f"ALTER TABLE {table_name} ADD {column};"
            self.cursor.execute(sql_statement)
        except pymysql.err.ProgrammingError:
            raise pymysql.err.ProgrammingError(
                'You probably gave existing column name')

    def add_url(self, database_name, table_name, url):
        self.connection.select_db(database_name)
        sql_statement = f""
        self.cursor.execute(sql_statement)


class BlackListManager:
    def __init__(self, db, host='localhost', user='root', password='None', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password="",
            database='',
            charset=charset,
            cursorclass=cursorclass,
        )
        self.cursor = self.connection.cursor()
        if db != '':
            self.create_database(db)
            self.connection.select_db(db)

    def create_database(self, database_name):
        sql_statement = f"CREATE DATABASE IF NOT EXISTS {database_name};"
        self.cursor.execute(sql_statement)

    def create_table(self, table_name):
        sql_statement = f"CREATE TABLE IF NOT EXISTS {table_name}(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255));"
        self.cursor.execute(sql_statement)


bl_database = BlackListManager(db='black_list')
database = SqlDataManager()
columns = """(
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_pierwszego_dodania VARCHAR(33),
    ostatnia_aktualizacja VARCHAR(40),
    nazwa_firmy VARCHAR(40),
    strona_internetowa VARCHAR(40),
    e_mail VARCHAR(40) CHECK(LENGTH(e_mail)-LENGTH(REPLACE(e_mail,'@',''))>0),
    nr_telefonu VARCHAR(40),
    fax VARCHAR(40),
    ulica VARCHAR(40),
    miejscowosc VARCHAR(40),
    kod_pocztowy VARCHAR(40),
    krs VARCHAR(40),
    nip VARCHAR(40),
    regon VARCHAR(40),
    kapital_zakladowy VARCHAR(40),
    forma_prawna VARCHAR(40),
    data_rejestracji VARCHAR(40),
    ostatnia_zmiana_krs VARCHAR(40),
    reprezentacja VARCHAR(40),
    sposob_reprezentacji VARCHAR(40),
    sad VARCHAR(40),
    sygnatura VARCHAR(40),
    podstawowa_dzialalnosc VARCHAR(40),
    wspolnicy VARCHAR(40),
    zarzad VARCHAR(40),
    prokura VARCHAR(40)
)"""

add_col = ('wlasciciel VARCHAR(40)', 'test VARCHAR(40)')
column = 'test2 VARCHAR(40)'
# database.create_database('testowa_baza_2')
# database.delete_database('baza_firm')
# database.create_table('baza_firm', 'nazwy', columns)
# database.add_columns('baza_firm', 'nazwy', columns)
# database.add_column('baza_firm', 'nazwy', column)
# database.delete_table('baza_firm', 'nazwy')
