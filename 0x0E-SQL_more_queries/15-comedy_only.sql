-- List comedy shows
SELECT
	tv_show.title
FROM
	tv_shows AS tv_show
INNER JOIN
	tv_show_genres AS show_genre
		ON show_genre.show_id = tv_show.id
INNER JOIN
	tv_genres AS genre
		ON genre.id = show_genre.genre_id
WHERE
	genre.name = "Comedy"
ORDER BY
	tv_show.title ASC
;
