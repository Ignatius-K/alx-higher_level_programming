-- List all records of table `second_table`
-- don't list rows without `name`
-- Display `score`, `name` in this order
-- Listed by descending score
SELECT score, name
	FROM second_table
	WHERE name IS NOT NULL
	ORDER BY score DESC;
