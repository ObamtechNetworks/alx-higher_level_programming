-- a script that uses the hbtn_0d_tvshows database
-- to list all shows without Comedy

-- List Shows without Comedy Genres
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.title NOT IN (
SELECT tv_shows.title
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title ASC;
