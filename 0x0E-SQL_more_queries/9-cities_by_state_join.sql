-- List all cities in database `hbtn_0d_usa`
-- Display; `cities.id`, `cities.name`, `states.name`
SELECT
	cities.id,
	cities.name,
	states.name
FROM
	cities
LEFT JOIN
	states ON cities.state_id = states.id
