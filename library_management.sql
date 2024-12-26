CREATE TABLE Books ( 
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL, 
    author VARCHAR(255) NOT NULL, 
    published_date DATE, genre VARCHAR(100),
    quantity INT NOT NULL ); 
CREATE TABLE Members ( 
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL, 
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL );