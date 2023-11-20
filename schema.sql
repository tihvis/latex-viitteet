CREATE TABLE citations (
	id SERIAL PRIMARY KEY,
	type TEXT,
);
CREATE TABLE books (
	citation_id INTEGER,
	publisher TEXT,
	/* more cols here */
	FOREIGN KEY (citation_id) REFERENCES citations (citation_id),
);
CREATE TABLE authors (
	id SERIAL PRIMARY KEY,
	name TEXT,
);
CREATE TABLE authors_citations (
	author_id TEXT REFERENCES authors (author_id), 
	citation_id REFERENCES citations (citation_id),
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL UNIQUE,
	password TEXT,
);
