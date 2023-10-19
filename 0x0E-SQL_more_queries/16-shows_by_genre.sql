-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.

Select tv_shows.title, tv_genres.name
From tv_shows
Left jOiN tv_show_genres
on tv_shows.id = tv_show_genres.show_id
Left JoiN tv_genres
On tv_show_genres.genre_id = tv_genres.id
OrdeR bY tv_shows.title, tv_genres.name;
