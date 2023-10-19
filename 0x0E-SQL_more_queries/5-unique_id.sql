-- script that creates the table unique_id on your MySQL server.

create table if not exists unique_id (id INT unique default 1, name VARCHAR(256));
