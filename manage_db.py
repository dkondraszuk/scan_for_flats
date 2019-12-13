import sqlite3

DB_FILE = 'flats.db'


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(f"Error during connecting to database file '{db_file}' : {e}")
    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(f"Error during creating table with sql statement '{create_table_sql}' : {e}")


def main():
    sql_create_previous_flats_status = """ CREATE TABLE IF NOT EXISTS PreviousStatus (
                                            floor integer PRIMARY KEY,
                                            status text NOT NULL,
                                            price integer NOT NULL
                                    );"""

    sql_create_current_flats_status = """ CREATE TABLE IF NOT EXISTS CurrentStatus (
                                            floor integer PRIMARY KEY,
                                            status text NOT NULL,
                                            price integer NOT NULL,
                                            prev_floor integer NOT NULL,
                                            FOREIGN KEY (prev_floor) REFERENCES PreviousStatus (floor)
                                    );"""

    conn = create_connection(DB_FILE)
    if conn is not None:
        create_table(conn, sql_create_previous_flats_status)
        create_table(conn, sql_create_current_flats_status)
    else:
        print('Error! Cannot create database connection!')


if __name__ == '__main__':
    main()
