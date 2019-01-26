import psycopg2

connection = psycopg2.connect(database="learning", user = "postgres", password = "P@ssw0rd", host = "localhost")

cursor = connection.cursor()
cursor.execute("SELECT * FROM purchases")

for row in cursor:
    print(row)