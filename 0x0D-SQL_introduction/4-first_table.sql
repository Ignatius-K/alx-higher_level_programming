-- Create table called `first_table` in current database
-- With columns; id, name
-- If the table does not exist
-- Database name passed as an argument
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
