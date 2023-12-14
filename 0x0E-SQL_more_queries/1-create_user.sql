-- a script that creates the user user_0d_1 and grant all privileges to user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT SELECT, INSERT, UPDATE, DELETE ON mysql.* TO 'user_0d_1'@'localhost';
