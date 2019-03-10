import psycopg2
import secrets

db = 'brucewilly'
def create_table():
    conn = psycopg2.connect(dbname=db, port = '5432', **secrets.database_login)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS store")
    cur.execute("CREATE TABLE store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect(dbname=db, port = '5432', **secrets.database_login)
    cur = conn.cursor()
    #cur.execute("INSERT INTO store(item, quantity, price) VALUES ('%s','%s','%s')" % (item, quantity, price)) # prone to SQL injection attack
    cur.execute("INSERT INTO store(item, quantity, price) VALUES (%s,%s,%s)", (item, quantity, price)) # Good
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect(dbname=db, port = '5432', **secrets.database_login)
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect(dbname=db, port = '5432', **secrets.database_login)
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = psycopg2.connect(dbname=db, port = '5432', **secrets.database_login)
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()

create_table()
insert("Rathat", 100, 199.99)
insert("Goatskin Chaps", 2, 1999.99)
print(view())

delete("Rathat")
update(4, 2099.99, 'Goatskin Chaps')
print(view())
