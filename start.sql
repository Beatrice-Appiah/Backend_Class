/* A database is a structured or unstructired collection of data accesed by the backend server.
a. It also stores data permanently.
b. It is used when working with large amount of data.

There are two types of Databases:
-Relational DataBase Management Syatem: This stores data using tables. 
Examples; MySQL, PostgreSQL,SQLite.
-Non-relational Database Management System: This used to work with large and unstructired data 
With this data is stored as document,key value pairs or graphs.
Examples; Mongodb, CassandraDB. */

-- MySQl is a sub of SQL and this a query language. ROW - RECORD, COLUMN - FIELD

-- Creating a Database
CREATE DATABASE IF NOT EXISTS my_class;

/* Entering a the mysql terminal, "-u root" is the root user
sudo -u root -p */

/* Showing all databases
SHOW DATABASES */


-- Selecting a particular database to use
USE my_class;

-- Creating Tables in Database
CREATE TABLE IF NOT EXISTS T4G (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO T4G (user_name,email)
VALUES ('me', 'me@gmail'),
('you', 'you@gmail.com');


/* DATA TYPES--
 VARCHAR(256): This takes an argument as a specific
 INT: Takes an argument as an integer
 BOOLEAN: Takes an argument as TRUE or FALSE values.
 FLOAT: Takes an argument as a decimal
 DECIMAL: Takes an argument where it is a larger float. 
 DATE  */

/* CONSTRAINTS-- They help set limitations or restrictions for a specific column. 
                  This makes sure a user does not insert wrong data.
 NOT NULL
 Primary Key: For referencing and usually to set IDs. This is a combination of UNIQUE and NOT NULL constraints.
 UNIQUE: This makes sure there column values for the tables are unique.
 AUTO_INCREMENT: this automatically increases a column value. */

/* NOTE: There can be only one PRIMARY KEY for a table */


alwys add .first, after using 'filter by'