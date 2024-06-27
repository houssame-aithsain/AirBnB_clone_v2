-- Check if the database exists, and create it if it does not
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Check if the user exists, and create if it does not
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the specified database to the user
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privileges on the performance schema to the user
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
