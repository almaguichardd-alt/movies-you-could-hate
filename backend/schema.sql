-- create SQL database schema
CREATE TABLE Movie (
  movie_id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  violence_level INTEGER CHECK (violence_level BETWEEN 1 AND 5),
  pacing INTEGER CHECK (pacing BETWEEN 1 AND 5),
  tone INTEGER CHECK (tone BETWEEN 1 AND 5)
);

CREATE TABLE Genre (
    genre_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE MovieGenre (
    movie_id INTEGER REFERENCES Movie(movie_id) ON DELETE CASCADE,
    genre_id INTEGER REFERENCES Genre(genre_id) ON DELETE CASCADE,
    PRIMARY KEY (movie_id, genre_id)
);

CREATE TABLE Person (
    person_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    role TEXT CHECK (role IN ('actor', 'director')) NOT NULL
);

CREATE TABLE MoviePerson (
    movie_id INTEGER REFERENCES Movie(movie_id) ON DELETE CASCADE,
    person_id INTEGER REFERENCES Person(person_id) ON DELETE CASCADE,
    PRIMARY KEY (movie_id, person_id)
);
