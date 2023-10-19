--  script that lists all shows from hbtn_0d_tvshows_rate by their rating.

Select tv_shows.title, SUM(tv_show_ratings.rate) As rating
From tv_shows
Inner JoiN tv_show_ratings
On tv_shows.id = tv_show_ratings.show_id
Group bY tv_shows.id
Order bY rating DESC;
