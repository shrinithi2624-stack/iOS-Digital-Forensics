
import sqlite3

# Connect to the iOS forensic database
conn = sqlite3.connect("ios_records.db")
cursor = conn.cursor()

print("=" * 50)
print("       iOS DIGITAL FORENSIC REPORT")
print("=" * 50)

# Parse Contacts
print("\n[1] EXTRACTED CONTACT RECORDS")

cursor.execute("SELECT * FROM contacts")

contacts = cursor.fetchall()

if contacts:
    for record in contacts:
        print("Contact ID :", record[0])
        print("Name       :", record[1])
        print("Phone      :", record[2])
        print("-" * 30)
else:
    print("No contact records found.")

# Parse Messages
print("\n[2] EXTRACTED MESSAGE RECORDS")

cursor.execute("SELECT * FROM messages")

messages = cursor.fetchall()

if messages:
    for record in messages:
        print("Message ID :", record[0])
        print("Sender     :", record[1])
        print("Message    :", record[2])
        print("Timestamp  :", record[3])
        print("-" * 30)
else:
    print("No message records found.")

# Display summary
print("\n[3] FORENSIC SUMMARY")
print("Total Contacts :", len(contacts))
print("Total Messages:", len(messages))

conn.close()

print("\nRecords parsed successfully.")
print("Forensic analysis completed.")

# Generate forensic report
with open("iOS_Forensic_Report.txt", "w") as file:

    file.write("iOS DIGITAL FORENSIC REPORT\n")
    file.write("=" * 40 + "\n\n")

    file.write("CONTACT RECORDS\n")
    file.write("-" * 30 + "\n")

    for record in contacts:
        file.write(
            f"ID: {record[0]} | "
            f"Name: {record[1]} | "
            f"Phone: {record[2]}\n"
        )

    file.write("\nMESSAGE RECORDS\n")
    file.write("-" * 30 + "\n")

    for record in messages:
        file.write(
            f"ID: {record[0]} | "
            f"Sender: {record[1]} | "
            f"Message: {record[2]} | "
            f"Timestamp: {record[3]}\n"
        )

    file.write("\nFORENSIC SUMMARY\n")
    file.write(f"Total Contacts: {len(contacts)}\n")
    file.write(f"Total Messages: {len(messages)}\n")
    file.write("\nAnalysis completed successfully.\n")

print("Forensic report saved as iOS_Forensic_Report.txt")
