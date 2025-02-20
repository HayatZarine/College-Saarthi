import sqlite3

# Function to create database and add sample books
def init_db():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL
        )
    ''')

    # Sample book data
    books_data = [
        ("Data Structures and Algorithms", "Narasimha Karumanchi"),
        ("Introduction to Machine Learning", "Ethem Alpaydin"),
        ("Database System Concepts", "Silberschatz, Korth, Sudarshan"),
        ("Artificial Intelligence: A Modern Approach", "Stuart Russell, Peter Norvig"),
        ("Computer Networks", "Andrew S. Tanenbaum")
    ]

    cursor.executemany("INSERT INTO books (title, author) VALUES (?, ?)", books_data)

    conn.commit()
    conn.close()
    print("Database initialized successfully!")

# Function to fetch books matching a search query
def get_books(query):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT title, author FROM books WHERE title LIKE ?", ('%' + query + '%',))
    results = cursor.fetchall()
    
    conn.close()
    return results



from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"

