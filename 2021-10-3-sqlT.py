import sqlite3
# db_name = 
conn = sqlite3.connect(db_name)
cursor = conn.cursor()
def firstTimeDB():
    sql = 'CREATE TABLE tablename (task TEXT)'
    runSql(sql)
    
if not os.path.isfile('tablename.db')
    firstTimeDB()
#query
sql = 'SELECT * FROM tablename'
cursor.execute(sql)
cursor.fetchall()
#delete insert update
sql = ''
value = (data,)
cursor.execute(sql,data)
conn.commit()

