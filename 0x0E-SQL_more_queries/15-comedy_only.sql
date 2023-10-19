-- script that lists all Comedy shows in the database hbtn_0d_tvshows.

Select tv_shows.title
From tv_shows
Inner JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
Inner JOIN tv_genres
On tv_show_genres.genre_id = tv_genres.id
WherE tv_genres.name = "Comedy"
ORder BY tv_shows.title;
