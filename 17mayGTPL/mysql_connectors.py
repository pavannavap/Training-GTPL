import mysql.connector

# Replace with your MySQL connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pava1.@143",
    database="pavan"
)

mycursor = mydb.cursor()

# Execute a query (replace with your desired query)
mycursor.execute("SHOW SCHEMAS")
# mycursor.execute("create schema GTPL_internship")

# Fetch results
myresult = mycursor.fetchall()

# Print results (optional)
for row in myresult:
    print(row)

# Close connections (important)
mycursor.close()
mydb.close()
