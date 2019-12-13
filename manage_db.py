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
    sql_create_statuses_table = """ CREATE TABLE IF NOT EXISTS statuses (
                                            floor integer PRIMARY KEY,
                                            prev_status text NOT NULL,
                                            curr_status text NOT NULL,
                                            prev_price integer NOT NULL,
                                            curr_price integer NOT NULL
                                    );"""

    conn = create_connection(DB_FILE)
    if conn is not None:
        create_table(conn, sql_create_statuses_table)
    else:
        print('Error! Cannot create database connection!')


if __name__ == '__main__':
    main()
