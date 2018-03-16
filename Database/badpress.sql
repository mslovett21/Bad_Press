DROP DATABASE badpress;
CREATE DATABASE badpress;
USE badpress;

CREATE TABLE source(
	id INT NOT NULL,
	name VARCHAR(30),
	URL_logo VARCHAR(250),
	PRIMARY KEY(id)
);

CREATE TABLE state(
	id INT NOT NULL,
	name VARCHAR(50),
	URL_flag VARCHAR(250),
	primaries_date VARCHAR(50),
	PRIMARY KEY(id)
);


CREATE TABLE issue(
	id INT NOT NULL,
	name VARCHAR(50),
	info TEXT,
	URL_logo VARCHAR(250),
	PRIMARY KEY(id)
);

CREATE TABLE candidate(
	id INT NOT NULL,
	name VARCHAR(70),
	state_fk INT,
	date_birth VARCHAR(30),
	place_birth VARCHAR(100),
	position VARCHAR(100),
	URL_photo VARCHAR(250),
    party VARCHAR(50),
	score_issue_1 FLOAT,
	score_issue_2 FLOAT,
	score_issue_3 FLOAT,
	score_issue_4 FLOAT,
	score_issue_5 FLOAT,	
	PRIMARY KEY(id),
	FOREIGN KEY(state_fk) REFERENCES state(id)
);


CREATE TABLE article(
	id INT NOT NULL,
	candidate_fk INT,
	state_fk INT,
	link VARCHAR(250),
	sentiment_score FLOAT,
	issue_fk INT,
	summary TEXT,
	date VARCHAR(140),
    title VARCHAR(300),
    source_fk INT,
	PRIMARY KEY(id),
	FOREIGN KEY(candidate_fk) REFERENCES  candidate(id),
	FOREIGN KEY(state_fk) REFERENCES state(id),
	FOREIGN KEY(issue_fk) REFERENCES issue(id)
);