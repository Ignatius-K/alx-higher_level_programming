-- List all shows
-- Order by tv_shows.title, tv_show_genres.genre_id
-- If show has no genre, display `NULL`
SELECT
	shows.title,
	show_genres.genre_id
FROM
	tv_shows AS shows
LEFT JOIN
	tv_show_genres as show_genres
		ON shows.id = show_genres.show_id
ORDER BY
	shows.title ASC, show_genres.genre_id ASC
;
