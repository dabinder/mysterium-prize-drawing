USE prizes;

CREATE TABLE IF NOT EXISTS attendees(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	badge_name VARCHAR(100) NOT NULL,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL
);
CREATE USER IF NOT EXISTS prize_drawing IDENTIFIED BY '123';
GRANT ALL PRIVILEGES ON prizes.* TO prize_drawing;