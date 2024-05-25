-- List all genres of show `Dexter`
-- Display `tv_genres.name`
-- Order by `tv_genres.name` ASC
SELECT
	genre.name
FROM
	tv_genres AS genre
INNER JOIN
	tv_show_genres AS show_genre
		ON genre.id = show_genre.genre_id
INNER JOIN
	tv_shows AS tv_show
		ON tv_show.id = show_genre.show_id
WHERE
	tv_show.title = "Dexter"
ORDER BY
	genre.name ASC
;
