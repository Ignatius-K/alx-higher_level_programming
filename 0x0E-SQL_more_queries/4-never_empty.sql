-- Create table `id_not_null`
-- With columns; id, name
-- Id can't be NULL, with default of 1
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT NOT NULL DEFAULT 1,
	name VARCHAR(256)
);
