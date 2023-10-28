import MySQLdb

# Create the connection object
connection = MySQLdb.connect(
    host="db",
    user="admin",
    password="admin",
    db="mydatabase",
)
# Create cursor
cursor = connection.cursor()
