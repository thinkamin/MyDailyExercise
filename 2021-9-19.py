import sqlite3 
import os 


def runQuery(sql,data=None,receive=False):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    if data:
        cursor.execute(sql,data)
    else:
        cursor.execute(sql)
    if receive:
        return cursor.fetchall()
    else:
        conn.commit()
    conn.close()

def firstTimeDB():
    create_tables = "CREATE TABLE tests (test TEXT)"
    runQuery(create_tables)
    default_task_query = 'INSERT INTO tests VALUES (?)'
    default_task_data = ("syl is a genius")
    runQuery(default_task_query,default_task_data)

if not os.path.isfile("test.db"):
    firstTimeDB()    

