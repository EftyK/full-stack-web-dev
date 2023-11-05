import sqlite3

# Establish a connection to the database file
conn = sqlite3.connect('simple.db')
cursor = conn.cursor()

# Example data to be inserted
data_to_insert = [
    (1, 'ifgi', 51.9689, 7.595469),
    (2,'Schloss', 51.963483, 7.616229),
    (3,'Hauptbahnhof', 51.957027, 7.6345)
]

# Insert the data into the 'locations' table
cursor.executemany('INSERT INTO locations (id, name, latitude, longitude) VALUES (?, ?, ?, ?)', data_to_insert)

# Commit the changes and close the connection
conn.commit()
conn.close()