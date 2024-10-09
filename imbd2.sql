-- Χρήση της βάσης δεδομένων

USE imbd2;

-- Δημιουργία του πίνακα movies
CREATE TABLE movies (
    movieId INT PRIMARY KEY,
    title VARCHAR(255),
    reldate INT
);

-- Δημιουργία του πίνακα ratings
CREATE TABLE ratings (
    userId INT,
    movieId INT,
    rating DECIMAL(3,2),
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);
