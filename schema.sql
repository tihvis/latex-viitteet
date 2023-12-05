CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username TEXT UNIQUE,
	password_hash TEXT
);

CREATE TABLE citations (
	id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES users ON DELETE CASCADE, 
	bibtex JSONB
);


CREATE UNIQUE INDEX cite_ind_unique ON citations((bibtex ->> 'type'),(bibtex ->> 'title'),(bibtex ->> 'year'));