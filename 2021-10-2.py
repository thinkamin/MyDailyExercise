import sqlite3

def firstrun():
    create_tables = 'CREATE TABLE tasks \
            (task TEXT)'
    runquery(create_tables)

def runquery(sql,data=None,recieve=False):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    if data:
        cursor.execute(sql,data)
    else:
        cursor.execute(sql)

    if recieve:
        return cursor.fetchall()
    else:
        conn.commit()
    conn.close()

sql = 'INSERT INTO tasks VALUES (?)'
data_lst = ['song','yuan','long']

# firstrun()
for data in data_lst:
    runquery(sql,(data,))



