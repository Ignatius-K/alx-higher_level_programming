-- Create table `unique_id`
-- With columns; `id`, `name`
-- id sh'd be with default value 1 and unique
CREATE TABLE IF NOT EXISTS unique_id (
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
);
