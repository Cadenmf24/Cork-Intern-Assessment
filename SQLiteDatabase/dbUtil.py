import os
import sqlite3


# Connects to the DB
def connect():
    
    return sqlite3.connect("CorkInternAssessment.db")

# Ussed to get one instance from a table
def exec_get_one(sql, args = {}):

    conn = connect()
    cur = conn.cursor()

    cur.execute(sql, args)

    one = cur.fetchone()

    conn.close()

    return one

# Returns a list of tuples from a table
def exec_get_all(sql, args={}):

    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    list_of_tuples = cur.fetchall()
    conn.close()
    return list_of_tuples


# Used for editing an existing row
def exec_commit(sql, args = {}):
    conn = connect()
    cur = conn.cursor()
    result = cur.execute(sql, args)
    conn.commit()
    conn.close()

    return result


# Used to populate the sql DB
def exec_sql_file(path):

    full_path = os.path.join(os.path.dirname(__file__), f'{path}')
    conn = connect()
    cur = conn.cursor()

    with open(full_path, 'r') as file:
        cur.execute(file.read())
    
    conn.commit()
    conn.close()


print(exec_get_all("SELECT COUNT(*) FROM movies"))