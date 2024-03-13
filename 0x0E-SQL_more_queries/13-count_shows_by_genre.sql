-- Lists all genres from hbtn_0d_tvshows
SELECT g.`name` AS `genre`, COUNT(s.`genre_id`) AS `number_of_shows`
	FROM `tv_genres` AS g
	INNER JOIN `tv_show_genres` AS s
	ON g.`id` = s.`genre_id`
	WHERE s.`genre_id` IS NOT NULL
	GROUP BY `genre`
ORDER BY `number_of_shows` DESC;