-- script that lists all shows contained in the database hbtn_0d_tvshows.

Select tv_shows.title, tv_show_genres.genre_id
From tv_shows
Left JOIn tv_show_genres
On tv_shows.id=tv_show_genres.show_id
Order By tv_shows.title, tv_show_genres.genre_id;
