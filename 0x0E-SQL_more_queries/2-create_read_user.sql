-- creates a database hbtn_0d_2
-- a script that creates database hbtn_0d_2 and the user user_0d_2

-- create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- use the database
USE hbtn_0d_2;

-- create user on the database
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- grant only select privilege
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- flush privileges
FLUSH PRIVILEGES;
