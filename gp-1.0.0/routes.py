

from flask import request, jsonify, render_template
from app.app import app
import json

# Load book data from a JSON file
def load_books():
    with open("app/books.json", "r") as file:
        return json.load(file)

@app.route('/')
def home():
    return render_template("book_recommendation.html")  # Ensure this file is in the `templates` folder

@app.route('/search', methods=['GET'])
def search_books():
    query = request.args.get('query', '').lower()  # Get search query from frontend

    books = load_books()

    # Filter books based on the search query (matching title, author, or subject)
    filtered_books = [
        book for book in books
        if query in book["title"].lower() or query in book["author"].lower() or query in book["subject"].lower()
    ]

    return jsonify({"books": filtered_books})  # Send results as JSON



