-- Check if the database exists, and create it if it does not
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Check if the user exists, and create it if it does not
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the development database to the development user
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

-- Additionally, grant SELECT privileges on the performance schema for performance monitoring
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';

-- Apply the changes immediately
FLUSH PRIVILEGES;
