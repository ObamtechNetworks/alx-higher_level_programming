-- prints full table description
-- shows current table description
SELECT TABLE_NAME, SQL
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEME = 'hbtn_0c_0'
AND TABLE_NAME = 'first_table';
