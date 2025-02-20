from flask import Flask, request, jsonify, render_template
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("flashcards.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS flashcards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            topic TEXT NOT NULL,
            next_review DATE
        )
    """)
    conn.commit()
    conn.close()

init_db()

# API to create a new flashcard
@app.route('/add_flashcard', methods=['POST'])
def add_flashcard():
    data = request.json
    conn = sqlite3.connect("flashcards.db")
    cursor = conn.cursor()
    next_review = (datetime.now() + timedelta(days=1)).date()
    cursor.execute("INSERT INTO flashcards (question, answer, topic, next_review) VALUES (?, ?, ?, ?)",
                   (data['question'], data['answer'], data['topic'], next_review))
    conn.commit()
    conn.close()
    return jsonify({"message": "Flashcard added!"})

# API to get flashcards by topic
@app.route('/get_flashcards/<topic>', methods=['GET'])
def get_flashcards(topic):
    conn = sqlite3.connect("flashcards.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flashcards WHERE topic = ?", (topic,))
    flashcards = cursor.fetchall()
    conn.close()
    return jsonify(flashcards)

# API to update a flashcard review schedule
@app.route('/review_flashcard/<int:id>', methods=['POST'])
def review_flashcard(id):
    review_data = request.json
    difficulty = review_data.get('difficulty', 'medium')

    # Spaced repetition logic
    if difficulty == 'easy':
        next_review = (datetime.now() + timedelta(days=4)).date()
    elif difficulty == 'medium':
        next_review = (datetime.now() + timedelta(days=2)).date()
    else:
        next_review = (datetime.now() + timedelta(days=1)).date()

    conn = sqlite3.connect("flashcards.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE flashcards SET next_review = ? WHERE id = ?", (next_review, id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Flashcard review updated!"})

def get_books(query):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT title, author FROM books WHERE title LIKE ?", ('%' + query + '%',))
    results = cursor.fetchall()
    
    conn.close()
    return results

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    if query:
        books = get_books(query)
        return jsonify(books)
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)

