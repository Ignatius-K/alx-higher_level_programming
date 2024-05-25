-- List all cities of California
-- Found in database `hbtn_0d_usa`
-- Result must be sorted by `cities.id` in ascending order
WITH california_id AS (
	SELECT
		id
	FROM
		states
	WHERE
		name = "California"
)

SELECT
	cities.*
FROM
	cities
WHERE
	state_id = (
		SELECT id FROM california_id
	)
ORDER BY
	cities.id ASC;
