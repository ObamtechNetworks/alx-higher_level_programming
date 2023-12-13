-- converts the database hbtn_0c_0 database to UTF8 (utf8mb4,
-- collate utf8mb4_unicode_ci)
-- the following are converted to UTF8
-- Database hbtn_0c_0, Table: first_table, Field: name in first_table

-- select a database
USE hbtn_0c_0;

-- FIRSTLY CONVERT THE DATABASE CHARACTER SET AND COLLATE
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- SECONDLY CONVERT THE FIRST TABLE IN database hbtn_0c_0 to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CONVERT THE name FIELD IN first_table to UTF8
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Explicitly set the id column to int)
ALTER TABLE first_table MODIFY id INT;
