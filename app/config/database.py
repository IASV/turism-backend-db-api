import MySQLdb

# Database configuration
db_config = {
    "host": "DB",
    "user": "admin",
    "password": "admin",
    "db": "mydatabase",
}

# Create a connection to the database
conn = MySQLdb.connect(**db_config)
