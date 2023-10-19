-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter.

Select tv_genres.name
From tv_genres
Where tv_genres.id NOT IN
(Select tv_genres.id
	From tv_genres
	Inner Joi tv_show_genres
	On tv_genres.id = tv_show_genres.genre_id
	Inner Join tv_shows
	On tv_show_genres.show_id = tv_shows.id
	Where tv_shows.title = "Dexter")
Order By tv_genres.name;
