-- script that lists all shows contained hbtn_od_tvshow

-- select the records to display
SELECT name AS genre,
COUNT(DISTINCT tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
