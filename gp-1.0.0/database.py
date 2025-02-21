import sqlite3

# Connect to SQLite database (creates library.db if not exists)
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create books table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        link TEXT NOT NULL
    )
''')

# Insert sample book data
books_data = [
    ("Advanced Engineering Mathematics by Kreyszig E", "https://archive.org/details/AdvancedEngineeringMathematicsKreyszigE.9thEdWiley20061245s"),
    ("Electrical Technology by B.L Thareja", "https://dl.ojocv.gov.et/admin_/book/a-textbook-of-electrical-technology-volume-i-basic-electrical-engineering-b-l-theraja.pdf"),
    ("Computer Networking: A Top-Down Approach", "https://www.ucg.ac.me/skladiste/blog_44233/objava_64433/fajlovi/Computer%20Networking%20_%20A%20Top%20Down%20Approach,%207th,%20converted.pdf"),
    ("Operating Systems Concepts", "https://os.ecci.ucr.ac.cr/slides/Abraham-Silberschatz-Operating-System-Concepts-10th-2018.pdf"),
    ("Artificial Intelligence: A Modern Approach", "https://people.engr.tamu.edu/guni/csce421/files/AI_Russell_Norvig.pdf")
]

cursor.executemany("INSERT INTO books (title, link) VALUES (?, ?)", books_data)

# Commit changes and close connection
conn.commit()
conn.close()

print("Database initialized successfully!")

