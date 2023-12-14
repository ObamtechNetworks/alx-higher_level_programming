-- creates the database hbtn_0d_usa and creates the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- use the database
USE hbtn_0d_usa;

-- create table states if not exists
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
);
