-- List show without genre linked
-- Order by tv_shows.title, tv_show_genres.genre_id
SELECT
	shows.title,
	show_genres.genre_id
FROM
	tv_shows AS shows
LEFT OUTER JOIN
	tv_show_genres AS show_genres
		ON shows.id = show_genres.show_id
WHERE
	show_genres.show_id IS NULL
ORDER BY
	shows.title ASC, show_genres.genre_id ASC
;
