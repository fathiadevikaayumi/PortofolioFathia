-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 14, 2026 at 02:46 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `login_db1`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(1, 'aya', '$2y$10$W4gkyq/thOMDm2MK19lXHu32CRJ8OAMr432lcb51rT9iRFeWB5.rS'),
(2, 'yuyu', '$2y$10$SgU12SAAZUG8DkXKtoHZjObcKeMmS5AHQVcN5xZfqKGZ49IQdTzPG'),
(3, 'yaya', '$2y$10$ONTTDg9lafV2ZVOK5Bs3aOt79G79YZvh/X9.UB0MgvKQy8GyKNCy.'),
(4, 'yay', '$2y$10$yq9yzZkiNZayW6V2xoKW5OHvctDdqemWfeltX5NtZNIeitSzxGkGu'),
(5, 'fathia ', '$2y$10$zunjV4ugKqKZ1uqjtgfdaOpD0rstiohQjTMa1llKTYtsh7ZIyeFum'),
(6, 'yeye', '$2y$10$j7LusBCGClaOtwVrmeVfieKEya6oRvxPm41YmFubTqv3RreByAIPK'),
(7, 'ayumi', '$2y$10$j81cfafy9jXbmR.dRcvpw.3BWhtpJM.AjfZl1jAagj4iWrLppY.I2');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
