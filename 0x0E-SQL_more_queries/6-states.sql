-- Create database `hbtn_0d_usa` and table `states`
-- Description of `states`;
--	id [INT, unique, auto generated, Primary key]
--	name [char, cant be null]
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256)
);
