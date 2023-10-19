-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.

Select tv_shows.title
From tv_shows
Where tv_shows.id NOT IN
(Select tv_shows.id
	From tv_shows
	Inner Join tv_show_genres
	On tv_shows.id = tv_show_genres.show_id
	Inner Join tv_genres
	On tv_show_genres.genre_id = tv_genres.id
	Where tv_genres.name = "Comedy")
Order By tv_shows.title;
