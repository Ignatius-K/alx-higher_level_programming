-- List all records with `score` >= 10 in table `second_table`
-- display score, name in this order
-- Ordered by score (top first)
SELECT score, name
	FROM second_table
WHERE score >= 10
ORDER BY score DESC;
