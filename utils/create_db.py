import sqlite3

# Establish a connection to a database file (create if not exists)
conn = sqlite3.connect('simple.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS locations (
        id INTEGER PRIMARY KEY,
        name TEXT,
        latitude REAL NOT NULL,
        longitude REAL NOT NULL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()