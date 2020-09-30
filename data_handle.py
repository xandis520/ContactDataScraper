import pymysql


class FileDataManager:
    def __init__(self, filename):
        self.filename = filename


class SqlDataManager:
    def __init__(self, host='localhost', user='root', password="", db='', charset='utf8mb4'):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database='',
            charset=charset,
            cursorclass=pymysql.cursors.DictCursor,
        )
        self.cursor = self.connection.cursor()
        if db != '':
            self.create_database(db)
            self.connection.select_db(db)

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

    def update_table(self, database_name, table_name, columns):
        self.connection.select_db(database_name)
        try:
            for column in columns:
                sql_statement = f"ALTER TABLE {table_name} ADD {column};"
                self.cursor.execute(sql_statement)
        except pymysql.err.ProgrammingError:
            print('You probably gave existing column name')

    def add_columns(self, database_name, table_name, columns):
        self.connection.select_db(database_name)
        try:
            sql_statement = f"ALTER TABLE {table_name} ADD {column};"
            self.cursor.execute(sql_statement)
        except pymysql.err.ProgrammingError:
            raise pymysql.err.ProgrammingError(
                'You probably gave existing column name')

    def add_urls(self, database_name, table_name, urls):
        self.connection.select_db(database_name)
        n = len(urls)
        if n > 1:
            values = ''
            for index, url in enumerate(urls):
                values += "('" + url + "')"
                if index != n - 1:
                    values += ', '
        else:
            values = "('" + urls[0] + "')"

        sql_statement = f"INSERT INTO {table_name} (`strona_internetowa`) VALUES {values};"
        self.cursor.execute(sql_statement)
        self.connection.commit()

    def check_if_exists(self, database_name, table_name, column_name, data):
        self.connection.select_db(database_name)
        sql_statement = f"SELECT id FROM {table_name} WHERE {column_name} = '{data}'"
        self.cursor.execute(sql_statement)
        id = self.cursor.fetchone()
        if id is not None:
            return True
        else:
            return False

    def get_row(self, database_name, table_name, column_name, data):
        self.connection.select_db(database_name)
        sql_statement = f"SELECT * FROM {table_name} WHERE {column_name} = '{data}'"
        self.cursor.execute(sql_statement)
        row = self.cursor.fetchone()
        return row

    def insert_data(self, database_name, table_name, columns='All', data='NULL'):
        pass



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

# add_col = ('wlasciciel VARCHAR(40)', 'test VARCHAR(40)')
columns = ['test2 VARCHAR(40)']
# database.create_database('baza_firm')
# database.delete_database('baza_firm')
# database.create_table('baza_firm', 'nazwy', columns)
# database.update_table('baza_firm', 'nazwy', columns)
# database.delete_table('baza_firm', 'nazwy')
# urls = ['www.google.pl']
# database.add_urls('baza_firm', 'nazwy', urls)
# print(database.check_if_exists('baza_firm', 'nazwy', 'strona_internetowa', 'www.google.pl'))
print(database.get_row('baza_firm', 'nazwy', 'strona_internetowa', 'www.google.pl'))