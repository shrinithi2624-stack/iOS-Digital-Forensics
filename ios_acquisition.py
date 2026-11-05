
import sqlite3

# Create a simulated iOS forensic database
conn = sqlite3.connect("ios_records.db")
cursor = conn.cursor()

# Create Contacts table
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    contact_id INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT
)
""")

# Create Messages table
cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    message_id INTEGER PRIMARY KEY,
    sender TEXT,
    message TEXT,
    timestamp TEXT
)
""")

# Insert sample forensic records
cursor.executemany("""
INSERT INTO contacts (name, phone)
VALUES (?, ?)
""", [
    ("Arun", "9876543210"),
    ("Priya", "9123456780")
])

cursor.executemany("""
INSERT INTO messages (sender, message, timestamp)
VALUES (?, ?, ?)
""", [
    ("Arun", "Meeting at 10 AM", "2026-11-04 09:30:00"),
    ("Priya", "Please call me", "2026-11-04 10:15:00")
])

conn.commit()
conn.close()

print("iOS forensic database created successfully.")
print("Evidence stored in ios_records.db")
