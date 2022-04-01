import sqlite3

con = sqlite3.connect("sausage.db")
cur = con.cursor()
cur.execute("INSERT INTO products (PK_ProductID, IndexProduct, NameProduct, Sort, GroupProduct) VALUES ('155', '1', 'adw', 'ad', 'ad')")
cur.execute("select * from products")
print(cur.fetchall())
con.commit()
