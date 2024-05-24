-- Create database `hbtn_0d_usa` and table `cities`
-- Description of `cities`;
--	id [INT, unique, auto generated, Primary key]
--	state_id [not null, FK referencing states]
--	name [char, cant be null]
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256),
	PRIMARY KEY (id),
	FOREIGN KEY (state_id)
		REFERENCES hbtn_0d_usa.states(id)
);
