import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL
    )
''')

# Sample Data
cursor.executemany("INSERT INTO books (title, author) VALUES (?, ?)", [
    ("Data Structures and Algorithms", "Narasimha Karumanchi"),
    ("Introduction to Machine Learning", "Ethem Alpaydin"),
    ("Database System Concepts", "Silberschatz, Korth, Sudarshan"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell, Peter Norvig"),
    ("Computer Networks", "Andrew S. Tanenbaum")
])

conn.commit()
conn.close()

