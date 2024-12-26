# Library Management System

A Flask API for managing a library, allowing CRUD operations for books and members. The API includes search functionality for books by title or author, pagination, and token-based authentication.

## How to Run the Project

### Prerequisites
- Python 3.x installed
- MySQL server installed and running
- Postman (or any other API testing tool)
(a) How to run the project.
    1.Install dependencies:
        pip install Flask mysql-connector-python
    2.Set up the database:
    3.Set environment variables:
    4.Run the application
        python app.py
API Endpoints
Books
  1.Create Book: POST /books
  2.Get Book: GET /books/<int:book_id>
  3.Update Book: PUT /books/<int:book_id>
  4.Delete Book: DELETE /books/<int:book_id>
  5.List Books with Search and Pagination: GET /books?search=<query>&page=<page>&per_page=<per_page>
Members
  1.Create Member: POST /members
  2.Get Member: GET /members/<int:member_id>
  3.Update Member: PUT /members/<int:member_id>
  4.Delete Member: DELETE /members/<int:member_id>

(b) The design choices made.
  1. Flask Framework
    Flask was chosen for its simplicity and flexibility, making it easy to develop and scale the API.
  2. MySQL Database
    MySQL is a widely-used relational database, known for its reliability and performance. It is well-suited for handling the structured data of the library management system.
  3. Environment Variables for Configuration
    Using environment variables for database configuration enhances security and flexibility. This allows for easy configuration changes without modifying the code.
  4. Token-Based Authentication
    Token-based authentication is implemented to ensure secure access to the API. This allows only authenticated users to perform CRUD operations, enhancing security.
  5. Search and Pagination
    Implemented search functionality for books by title or author and pagination to manage large sets of data. This enhances user experience and performance.

(c) Any assumptions or limitations.
  1.Assumptions
     1.The database schema is predefined, and the necessary tables are created before running the application.
     2.Environment variables are properly set up before starting the application.
     3.No third-party libraries are used beyond the specified dependencies.
  2.Limitations
    1.The API currently does not support advanced filtering or sorting of books and members.
    2.Token-based authentication is basic and may need further enhancements for production-level security.
    3.Error handling can be improved to provide more detailed feedback to the users.

Testing the API
Use Postman or any other API testing tool to test the endpoints. Sample requests and responses are provided in the documentation. Ensure to set the Content-Type header to application/json for POST and PUT requests.

Contribution
Contributions are welcome! Please fork the repository and submit a pull request with your changes.
