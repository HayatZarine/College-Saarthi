from flask import Blueprint, render_template, request, jsonify
from . import db
from .models import Book, Flashcard, ToDo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{"id": b.id, "title": b.title, "author": b.author} for b in books])

@main.route('/add_flashcard', methods=['POST'])
def add_flashcard():
    data = request.json
    flashcard = Flashcard(question=data['question'], answer=data['answer'])
    db.session.add(flashcard)
    db.session.commit()
    return jsonify({"message": "Flashcard added successfully!"})

@main.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task = request.json['task']
        new_task = ToDo(task=task)
        db.session.add(new_task)
        db.session.commit()
        return jsonify({"message": "Task added successfully!"})
    
    tasks = ToDo.query.all()
    return jsonify([{"id": t.id, "task": t.task, "complete": t.complete} for t in tasks])
