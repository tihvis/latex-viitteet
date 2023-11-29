CREATE TABLE citations (
	id SERIAL PRIMARY KEY,
	bibtex JSONB
);

CREATE UNIQUE INDEX cite_ind_unique ON citations((bibtex ->> 'type'),(bibtex ->> 'title'),(bibtex ->> 'year'));