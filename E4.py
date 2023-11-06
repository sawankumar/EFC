import sqlite3

# Create or connect to the database
conn = sqlite3.connect("my_database.db")
print("Opened database successfully")

# Create a table if it doesn't exist
conn.execute("CREATE TABLE IF NOT EXISTS Person (NAME TEXT, AGE INT, SALARY REAL)")
print("Table created successfully")

# Insert data into the table
conn.execute("INSERT INTO Person (NAME, AGE, SALARY) VALUES ('Harry', 32, 20000.00 )")
conn.execute("INSERT INTO Person (NAME, AGE, SALARY) VALUES ('Marry', 42, 20500.50 )")
print("Insert done successfully")

# Select and print data from the table
cursor = conn.execute("SELECT NAME, AGE, SALARY FROM Person")
for row in cursor:
    print(f"NAME = {row[0]}\tAGE = {row[1]}\tSALARY = {row[2]}")

# Update data in the table
conn.execute("UPDATE Person SET SALARY = 25000.00 WHERE NAME='Marry'")
conn.commit()
print("Update done successfully")

# Select and print updated data
cursor = conn.execute("SELECT NAME, AGE, SALARY FROM Person WHERE NAME = 'Marry'")
for row in cursor:
    print(f"NAME = {row[0]}\tAGE = {row[1]}\tSALARY = {row[2]}")

# Delete data from the table
conn.execute("DELETE FROM Person WHERE NAME = 'Harry'")
conn.commit()
print("Delete done successfully")

# Select and print remaining data from the table
cursor = conn.execute("SELECT NAME, AGE, SALARY FROM Person")
for row in cursor:
    print(f"NAME = {row[0]}\tAGE = {row[1]}\tSALARY = {row[2]}")

# Close the database connection
conn.close()
