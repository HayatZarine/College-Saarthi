from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Create SQLite database
def create_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS flashcards (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      question TEXT NOT NULL,
                      answer TEXT NOT NULL)''')
    conn.commit()
    conn.close()

create_db()  # Call this function to ensure the database is created

@app.route('/')
def home():
    return render_template('flashcards.html')

# API to add flashcards
@app.route('/add_flashcard', methods=['POST'])
def add_flashcard():
    data = request.json
    question = data.get('question')
    answer = data.get('answer')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO flashcards (question, answer) VALUES (?, ?)", (question, answer))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Flashcard added successfully'}), 201

# API to get all flashcards
@app.route('/get_flashcards', methods=['GET'])
def get_flashcards():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flashcards")
    flashcards = cursor.fetchall()
    conn.close()

    return jsonify({'flashcards': [{'id': row[0], 'question': row[1], 'answer': row[2]} for row in flashcards]})

if __name__ == '__main__':
    app.run(debug=True)
