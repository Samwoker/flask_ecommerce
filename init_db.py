import sqlite3

conn = sqlite3.connect('database.db')

# with open("models/database.sql") as f:
    # try:
    #     conn.executescript(f.read())
    # except Exception as e:
    #     print("SQL Error : ",e)

#testing

# conn.execute("INSERT into Users(username,password) values(?,?)",("Samuel","123456"))
# conn.commit()
# conn.close()

#testing display

# conn.row_factory = sqlite3.Row
# rows=conn.execute("Select * from Users").fetchall()
# for row in rows:
#     print(row['username'] , row['password'])
# conn.commit()
# conn.close()