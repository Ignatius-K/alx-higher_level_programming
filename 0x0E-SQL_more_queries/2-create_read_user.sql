-- Create database `hbtn_0d_2` and user `user_0d_2`
-- `user_0d_2` has only `SELECT` privilege in database `hbtn_0d_2`
-- If user and database dont exist

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS "user_0d_2"@"localhost"
	IDENTIFIED BY "user_0d_2_pwd";

GRANT SELECT ON hbtn_0d_2.* TO "user_0d_2"@"localhost";
