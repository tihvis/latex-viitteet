CREATE TABLE citations (
	id SERIAL PRIMARY KEY,
	entry_type TEXT,
	/* bibtex fields */
	address TEXT,
	annote TEXT,
	author TEXT, /* for completeness, not used */
	booktitle TEXT,
	chapter TEXT,
	crossref TEXT,
	edition TEXT,
	editor TEXT,
	howpublished TEXT,
	institution TEXT,
	journal TEXT,
	key TEXT,
	month TEXT,
	note TEXT,
	number TEXT,
	organization TEXT,
	pages TEXT,
	publisher TEXT,
	school TEXT,
	series TEXT,
	title TEXT,
	type TEXT,
	volume TEXT,
	year TEXT,
	/* commonly used non-standard fields */
	doi TEXT,
	isbn TEXT,
	/* keywords TEXT, how do we implement this? */
	url TEXT
);

CREATE TABLE authors (
	id SERIAL PRIMARY KEY,
	name TEXT
);

CREATE TABLE authors_citations (
	author_id INTEGER REFERENCES authors,
	citation_id INTEGER REFERENCES citations
);