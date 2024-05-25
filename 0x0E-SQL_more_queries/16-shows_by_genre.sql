-- List all shows, all genres linked to that show
-- Display `NULL` if show has no genre
-- Order by `tv_show.title`. `tv_genre.name` ascending
SELECT
	tv_show.title,
	genre.name
FROM
	tv_shows AS tv_show
LEFT JOIN
	tv_show_genres AS show_genre
		ON show_genre.show_id = tv_show.id
LEFT JOIN
	tv_genres AS genre
		ON genre.id = show_genre.genre_id
ORDER BY
	tv_show.title ASC, genre.name ASC
;
