import os
from flask import Flask, request, jsonify, abort
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Database configuration using environment variables
db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'Nikhil'),
    'database': os.getenv('DB_NAME', 'library_management')
}

# Database helper functions
def execute_query(query, params=None):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params or ())
        result = cursor.fetchall()
    except Error as e:
        print(f"Error: {e}")
        result = []
    finally:
        cursor.close()
        connection.close()
    return result

def execute_non_query(query, params=None):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(query, params or ())
        connection.commit()
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

# Routes for Books CRUD
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    if not data or 'title' not in data or 'author' not in data or 'quantity' not in data:
        abort(400, 'Title, Author, and Quantity are required.')

    query = """
        INSERT INTO Books (title, author, published_date, genre, quantity)
        VALUES (%s, %s, %s, %s, %s)
    """
    params = (data['title'], data['author'], data.get('published_date'), data.get('genre'), data['quantity'])
    execute_non_query(query, params)

    return jsonify({'message': 'Book added successfully.'}), 201

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    query = "SELECT * FROM Books WHERE id = %s"
    result = execute_query(query, (book_id,))
    if not result:
        abort(404, 'Book not found.')
    return jsonify(result[0])

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    if not data:
        abort(400, 'No data provided.')

    query = """
        UPDATE Books
        SET title = %s, author = %s, published_date = %s, genre = %s, quantity = %s
        WHERE id = %s
    """
    params = (
        data.get('title'), data.get('author'), data.get('published_date'),
        data.get('genre'), data.get('quantity'), book_id
    )
    execute_non_query(query, params)

    return jsonify({'message': 'Book updated successfully.'})

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    query = "DELETE FROM Books WHERE id = %s"
    execute_non_query(query, (book_id,))
    return '', 204

# Routes for Members CRUD
@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data or 'phone' not in data:
        abort(400, 'Name, Email, and Phone are required.')

    query = """
        INSERT INTO Members (name, email, phone)
        VALUES (%s, %s, %s)
    """
    params = (data['name'], data['email'], data['phone'])
    execute_non_query(query, params)

    return jsonify({'message': 'Member added successfully.'}), 201

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    query = "SELECT * FROM Members WHERE id = %s"
    result = execute_query(query, (member_id,))
    if not result:
        abort(404, 'Member not found.')
    return jsonify(result[0])

@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    data = request.get_json()
    if not data:
        abort(400, 'No data provided.')

    query = """
        UPDATE Members
        SET name = %s, email = %s, phone = %s
        WHERE id = %s
    """
    params = (
        data.get('name'), data.get('email'), data.get('phone'), member_id
    )
    execute_non_query(query, params)

    return jsonify({'message': 'Member updated successfully.'})

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    query = "DELETE FROM Members WHERE id = %s"
    execute_non_query(query, (member_id,))
    return '', 204

# Search and Pagination for Books
@app.route('/books', methods=['GET'])
def list_books():
    search = request.args.get('search')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))

    base_query = "SELECT * FROM Books"
    where_clause = ""
    params = []

    if search:
        where_clause = " WHERE title LIKE %s OR author LIKE %s"
        params.extend([f"%{search}%", f"%{search}%"])

    query = base_query + where_clause + " LIMIT %s OFFSET %s"
    params.extend([per_page, (page - 1) * per_page])

    result = execute_query(query, params)
    return jsonify(result)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
