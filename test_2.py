import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('NetPy.db')

# Create a cursor
cursor = conn.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS devices (
    ip TEXT PRIMARY KEY,
    id TEXT,
    pw TEXT
)
""")

# save the changes
conn.commit()

# Close the connection
conn.close()