-- List all genres
-- Display number of shows linked to genre
-- Display columns; genre, number_of_shows
-- Order by number_of_shows in descending
SELECT
	genres.name AS genre,
	COUNT(show_genres.show_id) AS number_of_shows
FROM
	tv_genres AS genres
INNER JOIN
	tv_show_genres AS show_genres
		ON genres.id = show_genres.genre_id
GROUP BY
	genres.name
ORDER BY
	number_of_shows DESC
;
