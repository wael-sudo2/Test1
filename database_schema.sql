-- File: database_schema.sql

-- Create table for extracted data
CREATE TABLE IF NOT EXISTS extracted_data (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2),
    brand VARCHAR(255),
    imageUrl TEXT,
    productUrl TEXT
);
