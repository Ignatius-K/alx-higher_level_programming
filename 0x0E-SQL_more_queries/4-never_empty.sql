-- Create table `force_name`
-- With columns; id, name
-- Id can't be NULL, with default of 1
CREATE TABLE IF NOT EXISTS force_name (
	id INT NOT NULL DEFAULT 1,
	name VARCHAR(256)
);
