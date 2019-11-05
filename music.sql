DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS songs;
DROP TABLE IF EXISTS albums;

CREATE TABLE artists(
    artist_name TEXT,
    artist_id INTEGER PRIMARY KEY);


CREATE TABLE albums(
       artist_id INTEGER,
       album_name TEXT,
       album_id INTEGER PRIMARY KEY
);

CREATE TABLE songs(
    song_id INTEGER PRIMARY KEY,
    song_name TEXT,
    artist_id INTEGER,
    album_id INTEGER,
    track_number INTEGER,
    track_duration INTEGER
);