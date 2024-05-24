-- List all cities of California
-- Found in database `hbtn_0d_usa`
-- Result must be sorted by `cities.id` in ascending order
WITH california_id as (
	SELECT
		id
	FROM
		hbtn_0d_usa.states
	WHERE
		name = "California"
)

SELECT
	*
FROM
	hbtn_0d_usa.cities 
WHERE
	state_id = (
		SELECT id FROM california_id
	);
