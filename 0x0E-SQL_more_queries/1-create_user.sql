-- script that creates the MySQL server user user_0d_1

Create User If Not Exists 'user_0d_1'@'localhost' 
Identified By 'user_0d_1_pwd';
Grant All Priviledges ON *.* TO 'user_0d_1'@'localhost';
