-- Create MySQL server user `user_0d_1`
-- User password should be set to `user_0d_1_pwd`
-- If user doesn't exist
CREATE USER IF NOT EXISTS "user_0d_1"@"localhost"
	IDENTIFIED BY "user_0d_1_pwd";

GRANT ALL ON *.* TO "user_0d_1"@"localhost";
