-- script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.

create DATABASE if not EXISTS hbtn_0d_usa;
create Table if NOT EXISTS hbtn_0d_usa.states (id INT not null primary key AUTO_INCREMENT,
name VARCHAR(256) not null);
