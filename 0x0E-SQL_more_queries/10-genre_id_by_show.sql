-- List all shows
-- Display tv_shows.title, tv_show_genres.genre_id
-- Result ordered by tv_shows.title, tv_show_genres.genre_id
SELECT
	shows.title,
	show_genres.genre_id
FROM
	tv_shows AS shows
INNER JOIN
	tv_show_genres AS show_genres
		ON shows.id = show_genres.show_id
ORDER BY
	shows.title ASC, show_genres.genre_id ASC
;
