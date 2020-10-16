import _sqlite3

#sql sorgularini cogaltilabilir

connection = _sqlite3.connect("chinook.db")


cursor = connection.execute("""SELECT FirstName, LastName
                                FROM customers WHERE city = 'Prague'""")

for row in cursor:
    print("First Name: " + row[0])
    print("Last Name: " + row[1])
    print("\n")

print("---" * 15)
print("\n")
cursor = connection.execute("SELECT * FROM customers ORDER BY FirstName")


for row in cursor:
    print("First Name: " + row[1])
    print("Last Name: " + row[2])
    print("\n")

print("---" * 15)
print("\n")

cursor = connection.execute("SELECT * FROM customers ORDER BY FirstName DESC")

for row in cursor:
    print("First Name: " + row[1])
    print("Last Name: " + row[2])
    print("\n")


cursor = connection.execute("""SELECT city, count(*) 
                            FROM customers 
                            GROUP BY city HAVING count(*)>1
                            ORDER BY count(*) DESC"""
                            )

for row in cursor:
    print("City: " + row[0])
    print("Count: " + str(row[1]))
    print("\n")


connection.close()
