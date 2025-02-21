from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

def get_books(query):
    """Fetch books from the database matching the search query."""
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT title, link FROM books WHERE title LIKE ?", ('%' + query + '%',))
    results = cursor.fetchall()
    
    conn.close()
    return results

@app.route('/')
def index():
    """Render the library page."""
    return render_template("library.html")

@app.route('/search', methods=['GET'])
def search():
    """Handle AJAX search requests."""
    query = request.args.get('q', '')
    if query:
        books = get_books(query)
        return jsonify(books)
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
