import sqlite3

conn = sqlite3.connect('test.db')
#
with open("models/database.sql") as f:
    try:
        conn.executescript(f.read())
    except Exception as e:
        print("SQL Error : ",e)

#testing
# conn.execute('ALTER TABLE Cart ADD COLUMN quantity INTEGER DEFAULT 1')
# conn.execute("DROP TABLE Cart")
# conn.execute("INSERT INTO Products(name,price,category,image_url,description) VALUES(?,?,?,?,?)",
#              ('Laptop',999.99,'electronics','img/laptop.jpg','High-performance laptop'))
# conn.execute("INSERT INTO Products(name,price,category,image_url,description) VALUES(?,?,?,?,?)",
#              ('Phone',59.99,'electronics','img/phone.jpg','High-Resolution Camera , 256 GB storage'))
# conn.execute("INSERT INTO Products(name,price,category,image_url,description) VALUES(?,?,?,?,?)",
#              ('Shoe',29.99,'Clothing','img/shoe.jpg','Modern brand'))
# conn.execute("INSERT INTO Products(name,price,category,image_url,description) VALUES(?,?,?,?,?)",
#              ('Watch',99.99,'electronics','img/watch.jpg','Classic'))
# conn.execute("INSERT INTO Products(name,price,category,image_url,description) VALUES(?,?,?,?,?)",
#              ('Airpods',9.99,'electronics','img/earpod.jpg','High-performance laptop'))
#
# conn.commit()
# conn.close()

#testing display

conn.row_factory = sqlite3.Row
rows=conn.execute("Select * from Cart").fetchall()
for row in rows:
    print(dict(row))
# conn.commit()
# conn.close()