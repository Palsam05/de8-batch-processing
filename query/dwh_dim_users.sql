DROP TABLE IF EXISTS dim_users;
CREATE TABLE dim_users(
	user_id INT NOT NULL,
	user_first_name VARCHAR(255) NOT NULL,
	user_last_name VARCHAR(255) NOT NULL,
	user_gender VARCHAR(50) NOT NULL,
	user_address VARCHAR(255),
	user_birthday DATE NOT NULL,
	user_join DATE NOT NULL,
	PRIMARY KEY (user_id)
);