import sqlite3

conn = sqlite3.connect('MiniEpic.db')
cursor = conn.cursor()


cursor.execute('''SELECT * FROM PhoneNumber ''')

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()