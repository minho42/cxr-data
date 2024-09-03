import csv
import sqlite3
import os

def create_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cxr_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name TEXT UNIQUE NOT NULL,
        label TEXT,
        age INTEGER,
        gender TEXT,
        position TEXT
    )
    ''')

def insert_data(cursor, row):
    cursor.execute('''
    INSERT INTO cxr_data (name, label, age, gender, position)
    VALUES (?, ?, ?, ?, ?)
    ''', (row['name'], row['label'], row['age'], row['gender'], row['position']))

def main():
    csv_file = 'data2.csv'
    db_file = 'db.sqlite3'

    # Check if CSV file exists
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found.")
        return

    # Connect to SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create table
    create_table(cursor)

    # Read CSV and insert data
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            insert_data(cursor, row)

    # Commit changes and close connection
    conn.commit()
    conn.close()

    print(f"Data from {csv_file} has been successfully imported into {db_file}.")

if __name__ == "__main__":
    main()