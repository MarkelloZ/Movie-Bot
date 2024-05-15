-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Εξυπηρετητής: localhost
-- Χρόνος δημιουργίας: 14 Μάη 2024 στις 23:44:20
-- Έκδοση διακομιστή: 8.0.28
-- Έκδοση PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Βάση δεδομένων: `imbd`
--

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `movie`
--

CREATE TABLE `movie` (
  `movie_id` int NOT NULL,
  `movie_title` varchar(100) DEFAULT NULL,
  `movie_time` int DEFAULT NULL,
  `movie_rel` int DEFAULT NULL,
  `movie_lang` varchar(100) DEFAULT NULL,
  `movie_mpaa` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Άδειασμα δεδομένων του πίνακα `movie`
--

INSERT INTO `movie` (`movie_id`, `movie_title`, `movie_time`, `movie_rel`, `movie_lang`, `movie_mpaa`) VALUES
(1, 'Inception', 133, 2024, 'English', 'PG-13'),
(2, 'Inception', 133, 2024, 'English', 'PG-13');

--
-- Ευρετήρια για άχρηστους πίνακες
--

--
-- Ευρετήρια για πίνακα `movie`
--
ALTER TABLE `movie`
  ADD PRIMARY KEY (`movie_id`);

--
-- AUTO_INCREMENT για άχρηστους πίνακες
--

--
-- AUTO_INCREMENT για πίνακα `movie`
--
ALTER TABLE `movie`
  MODIFY `movie_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
