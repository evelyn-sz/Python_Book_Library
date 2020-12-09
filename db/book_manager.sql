DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    id SERIAL PRIMARY KEY
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    publisher VARCHAR(255),
    author_id INT REFERENCES authors(id)
);

