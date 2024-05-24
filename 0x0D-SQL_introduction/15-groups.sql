-- List number of records with the same score in table `second_table`
-- Display `score`, number of records for score with label `number`
-- Sorted by number of records (descending)
SELECT score, COUNT(*) as number
	FROM second_table
	GROUP BY score
	ORDER BY number DESC;
