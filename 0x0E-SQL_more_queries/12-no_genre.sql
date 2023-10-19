--  script that lists all shows contained in hbtn_0d_tvshows without a genre linked.

Select tv_shows.title, tv_show_genres.genre_id
From tv_shows
Left Join tv_show_genres
On tv_shows.id=tv_show_genres.show_id
Where tv_show_genres.show_id Is Null
Order By tv_shows.title, tv_show_genres.genre_id;
