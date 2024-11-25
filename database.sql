CREATE DATABASE inventory_db;
USE inventory_db;

CREATE TABLE items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    category VARCHAR(50),
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
); 