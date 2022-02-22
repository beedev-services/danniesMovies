-- phpMyAdmin SQL Dump
-- version 4.9.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 21, 2022 at 07:15 PM
-- Server version: 5.7.35-cll-lve
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `thehives_levan`
--

-- --------------------------------------------------------

--
-- Table structure for table `app_dvd`
--

CREATE TABLE `app_dvd` (
  `id` bigint(20) NOT NULL,
  `title` varchar(255) NOT NULL,
  `genre` varchar(255) NOT NULL,
  `actors` longtext NOT NULL,
  `year` varchar(255) NOT NULL,
  `misc` longtext NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app_dvd`
--

INSERT INTO `app_dvd` (`id`, `title`, `genre`, `actors`, `year`, `misc`, `user_id`) VALUES
(1, 'A Smokey Mountain Christmas', 'Fantasy/Music', 'Dolly Parton, Lee Majors, John Ritter, Anita Morris', '1986', '', 1),
(2, 'American Sweethearts', 'Romance/Comedy', 'Julia Roberts, Catherine Zeta-Jones, John Cusack', '2001', '', 1),
(3, 'Assassins', 'Action/Crime', 'Antonio Banderas, Sylvester Stallone', '1995', '', 1),
(4, 'A Walk To Remember', 'Romance/Drama', 'Mandy Moore, Shane West', '2002', '', 1),
(5, 'The Lake House', 'Romance/Fantasy', 'Sandra Bullock, Keanu Reeves', '2006', '', 1),
(6, 'A Christmas Story', 'Comedy/Kids/Family', 'Peter Billingsley, Zach Ward, Darren Mcgavin, Melinda Dillon, Ian Petrella, Scotty Schwartz, R.D. Robb', '1983', '', 1),
(7, 'A Christmas Story 2', 'Comedy/Kids/Family', 'Breaden Lemasters, Daniel Stern, Valin Shinyei, Stacey Travis', '2012', '', 1),
(8, 'Ace Ventura Pet Detective/ Ace Ventura When Nature Calls', 'Comedy/Mystery', 'Jim Carrey', '1994/1995', 'This Is a Box Set', 1),
(9, 'Attack Force', 'Action/Thriller', 'Steven Segal, Lisa Lovbrand, David Kennedy', '2006', '', 1),
(10, 'A Knight\'s Tale', 'Action/Adventure', 'Heath Ledger, Shanynn Sossamon, Mark Addy, Paul Bettany, Alan Tudyk', '2001', '', 1),
(11, 'An American Haunting', 'Horror/Mystery', 'Sissy Spacek, Donald Sutherland, Rachel Hurd-Wood, James D\'arcy', '2006', '', 1),
(12, 'As Good As it Gets', 'Romance/Comedy', 'Jack Nicholson, Greg Kinnear, Helen Hunt, ', '1997', '', 1),
(13, 'All The Pretty Horses', 'Western/Romance', 'Penelope Cruz, Matt Damon', '2000', '', 1),
(14, 'A Time To Remember', 'Drama/Family', 'Doris Roberts, Dana Delany', '2003', '', 1),
(15, 'Anger Management', 'Comedy/Slapstick', 'Adan Sandler, Jack Nicholson, Marisa Tomei, Woody Harrelson', '2003', '', 1),
(16, 'Along Came Polly', 'Romance/Comedy', 'Ben Stiller, Debra Messing', '2004', '', 1),
(17, 'A Wedding For Bella', 'Romance/Drama', 'Scott Baio, Kristin Minter', '2001', '', 1),
(18, 'Alf   ', 'Sitcom', 'Paul Fusco, Max Wright, Anne Schedeen, Andrea Elson, Benji Gregory', '1986', ' (Complete Series)', 1),
(19, 'A Walk Among The TombStones', 'Mystery/Thriller', 'Liam Neeson,', '2014', '', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `app_dvd`
--
ALTER TABLE `app_dvd`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app_dvd_user_id_cd6bf1f8` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `app_dvd`
--
ALTER TABLE `app_dvd`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
