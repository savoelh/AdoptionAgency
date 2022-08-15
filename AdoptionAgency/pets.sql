DROP DATABASE IF EXISTS pets;

CREATE DATABASE pets;

 \c pets

CREATE TABLE pets
(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    photo_url TEXT,
    age INTEGER,
    notes TEXT,
    available BOOLEAN 
);

INSERT INTO pets
(name, species, photo_url, age, notes, available)

VALUES
('Odin', 'cat', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/1200px-Cat_November_2010-1a.jpg', 10, 'Hes a monster kitty :3', 'f')