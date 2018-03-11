USE badpress;

CREATE TABLE source(
	id INT NOT NULL,
	name VARCHART(30),
	URL_logo VARCHART(250),
	PRIMARY KEY(id)
);

CREATE TABLE state(
	id INT NOT NULL,
	name VARCHART(50),
	URL_flag VARCHART(250),
	primaries_date VARCHART(50),
	PRIMARY KEY(id)
);


CREATE TABLE issue(
	id INT NOT NULL,
	name VARCHART(50),
	info TEXT,
	URL_logo VARCHART(250),
	PRIMARY KEY(id)
);

CREATE TABLE candidate(
	id INT NOT NULL,
	name VARCHART(70),
	state_fk INT,
	date_birth DATE,
	place_birth VARCHART(100),
	position VARCHART(100),
	office_address VARCHART(100),
	URL_photo VARCHART(250),
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
	link VARCHART(250),
	sentiment_score FLOAT,
	issue_fk INT,
	summary TEXT,
	date DATE,
	PRIMARY KEY(id),
	FOREIGN KEY(candidate_fk) REFERENCES  candidate(id),
	FOREIGN KEY(state_fk) REFERENCES state(id),
	FOREIGN KEY(issue_fk) REFERENCES issue(id)
);