CREATE TABLE citations (
	id SERIAL PRIMARY KEY,
	type TEXT,
	title TEXT,
	year INTEGER
);

CREATE TABLE articles (
	id INTEGER,
	journal TEXT,
	volume TEXT, /* these are strings in bibtex */
	number TEXT,
	pages TEXT,
	FOREIGN KEY (id) REFERENCES citations(id)
);

CREATE TABLE books (
	id INTEGER,
	publisher TEXT,
	address TEXT,
	FOREIGN KEY (id) REFERENCES citations(id)	
);

CREATE TABLE inproceedings (
	id INTEGER,
	booktitle TEXT,
	series TEXT,
	pages TEXT,
	publisher TEXT,
	FOREIGN KEY (id) REFERENCES citations(id)	
);

CREATE TABLE authors (
	id SERIAL PRIMARY KEY,
	name TEXT
);

CREATE TABLE authors_citations (
	author_id INTEGER REFERENCES authors,
	citation_id INTEGER REFERENCES citations
);