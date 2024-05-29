-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 28, 2024 at 08:47 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `customer_invoices`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer_invoices`
--

CREATE TABLE `customer_invoices` (
  `invoice_id` int(11) NOT NULL,
  `customer_name` varchar(50) NOT NULL,
  `amount` decimal(10,0) DEFAULT NULL,
  `invoice_date` datetime DEFAULT NULL,
  `contact_number` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer_invoices`
--

INSERT INTO `customer_invoices` (`invoice_id`, `customer_name`, `amount`, `invoice_date`, `contact_number`) VALUES
(1, 'devend', 2345, '2023-09-21 00:00:00', '9856475213'),
(2, 'shubh', 5000, '2024-01-17 07:35:07', '8855221789'),
(3, 'raj', 2345, '2024-05-24 11:51:48', '9652314569'),
(4, 'Rama', 9800, '2024-05-24 11:52:11', '9856321475'),
(6, 'Arjun', 2345, '2024-05-28 11:16:14', '8954123654'),
(7, 'Ashwini', 3456, '2024-05-28 11:17:23', '7896541236'),
(8, 'yatri', 5600, '2024-05-28 11:17:37', '8974563210'),
(9, 'krupal', 4500, '2024-05-28 11:18:41', '9874562134'),
(10, 'Rishit', 6700, '2024-05-28 11:18:56', '8965412378');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer_invoices`
--
ALTER TABLE `customer_invoices`
  ADD PRIMARY KEY (`invoice_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer_invoices`
--
ALTER TABLE `customer_invoices`
  MODIFY `invoice_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
