-- a script that creates the user user_0d_1 and
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON mysql.* TO 'user_0d_1'@'localhost';
