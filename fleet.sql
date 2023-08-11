-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 11, 2023 at 05:26 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fleet`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_customuser'),
(22, 'Can change user', 6, 'change_customuser'),
(23, 'Can delete user', 6, 'delete_customuser'),
(24, 'Can view user', 6, 'view_customuser'),
(25, 'Can add car', 7, 'add_car'),
(26, 'Can change car', 7, 'change_car'),
(27, 'Can delete car', 7, 'delete_car'),
(28, 'Can view car', 7, 'view_car'),
(29, 'Can add car model', 8, 'add_carmodel'),
(30, 'Can change car model', 8, 'change_carmodel'),
(31, 'Can delete car model', 8, 'delete_carmodel'),
(32, 'Can view car model', 8, 'view_carmodel'),
(33, 'Can add car make', 9, 'add_carmake'),
(34, 'Can change car make', 9, 'change_carmake'),
(35, 'Can delete car make', 9, 'delete_carmake'),
(36, 'Can view car make', 9, 'view_carmake'),
(37, 'Can add car class', 10, 'add_carclass'),
(38, 'Can change car class', 10, 'change_carclass'),
(39, 'Can delete car class', 10, 'delete_carclass'),
(40, 'Can view car class', 10, 'view_carclass'),
(41, 'Can add client', 11, 'add_client'),
(42, 'Can change client', 11, 'change_client'),
(43, 'Can delete client', 11, 'delete_client'),
(44, 'Can view client', 11, 'view_client'),
(45, 'Can add reservation', 12, 'add_reservation'),
(46, 'Can change reservation', 12, 'change_reservation'),
(47, 'Can delete reservation', 12, 'delete_reservation'),
(48, 'Can view reservation', 12, 'view_reservation'),
(49, 'Can add driver', 13, 'add_driver'),
(50, 'Can change driver', 13, 'change_driver'),
(51, 'Can delete driver', 13, 'delete_driver'),
(52, 'Can view driver', 13, 'view_driver'),
(53, 'Can add taxes', 14, 'add_taxes'),
(54, 'Can change taxes', 14, 'change_taxes'),
(55, 'Can delete taxes', 14, 'delete_taxes'),
(56, 'Can view taxes', 14, 'view_taxes'),
(57, 'Can add car out', 15, 'add_carout'),
(58, 'Can change car out', 15, 'change_carout'),
(59, 'Can delete car out', 15, 'delete_carout'),
(60, 'Can view car out', 15, 'view_carout'),
(61, 'Can add payment method', 16, 'add_paymentmethod'),
(62, 'Can change payment method', 16, 'change_paymentmethod'),
(63, 'Can delete payment method', 16, 'delete_paymentmethod'),
(64, 'Can view payment method', 16, 'view_paymentmethod'),
(65, 'Can add inspection item status', 17, 'add_inspectionitemstatus'),
(66, 'Can change inspection item status', 17, 'change_inspectionitemstatus'),
(67, 'Can delete inspection item status', 17, 'delete_inspectionitemstatus'),
(68, 'Can view inspection item status', 17, 'view_inspectionitemstatus'),
(69, 'Can add inspection item', 18, 'add_inspectionitem'),
(70, 'Can change inspection item', 18, 'change_inspectionitem'),
(71, 'Can delete inspection item', 18, 'delete_inspectionitem'),
(72, 'Can view inspection item', 18, 'view_inspectionitem'),
(73, 'Can add car inspection', 19, 'add_carinspection'),
(74, 'Can change car inspection', 19, 'change_carinspection'),
(75, 'Can delete car inspection', 19, 'delete_carinspection'),
(76, 'Can view car inspection', 19, 'view_carinspection'),
(77, 'Can add fuel', 20, 'add_fuel'),
(78, 'Can change fuel', 20, 'change_fuel'),
(79, 'Can delete fuel', 20, 'delete_fuel'),
(80, 'Can view fuel', 20, 'view_fuel');

-- --------------------------------------------------------

--
-- Table structure for table `car_car`
--

CREATE TABLE `car_car` (
  `id` bigint(20) NOT NULL,
  `number_plate` varchar(20) NOT NULL,
  `model_id` bigint(20) DEFAULT NULL,
  `year` int(10) UNSIGNED NOT NULL,
  `color` varchar(50) NOT NULL,
  `daily_rate` decimal(8,2) NOT NULL,
  `seating_capacity` int(10) UNSIGNED NOT NULL CHECK (`seating_capacity` >= 0),
  `image` varchar(100) DEFAULT NULL,
  `make_id` bigint(20) DEFAULT NULL,
  `car_class_id` bigint(20) DEFAULT NULL,
  `monthly_rate` decimal(8,2) DEFAULT NULL,
  `weekly_rate` decimal(8,2) DEFAULT NULL,
  `mileage` int(10) UNSIGNED DEFAULT NULL CHECK (`mileage` >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `car_car`
--

INSERT INTO `car_car` (`id`, `number_plate`, `model_id`, `year`, `color`, `daily_rate`, `seating_capacity`, `image`, `make_id`, `car_class_id`, `monthly_rate`, `weekly_rate`, `mileage`) VALUES
(1, 'ABC123', 1, 2022, 'white', 30.00, 4, 'car_images/1_YD45FLI.png', 1, 8, 20.00, 25.00, 0),
(2, 'GHI789', 2, 2020, 'white', 30.00, 4, 'car_images/2.png', 1, 8, 20.00, 25.00, 0),
(3, 'YZA901', 9, 2022, 'Silver', 45.00, 4, 'car_images/3.png', 13, 4, 35.00, 40.00, 0);

-- --------------------------------------------------------

--
-- Table structure for table `car_carclass`
--

CREATE TABLE `car_carclass` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `car_carclass`
--

INSERT INTO `car_carclass` (`id`, `name`) VALUES
(1, 'Buses'),
(2, 'Double Cabin'),
(3, 'Single Cabin'),
(4, 'Large SUV'),
(5, 'Minivan'),
(6, 'Safari 4WD'),
(7, 'Saloon'),
(8, 'Small SUV');

-- --------------------------------------------------------

--
-- Table structure for table `car_carmake`
--

CREATE TABLE `car_carmake` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `car_carmake`
--

INSERT INTO `car_carmake` (`id`, `name`) VALUES
(1, 'Toyota'),
(2, 'Ford'),
(3, 'Honda'),
(4, 'Mercedes-Benz'),
(5, 'BMW'),
(6, 'Volkswagen'),
(7, 'Nissan'),
(8, 'Chevrolet'),
(9, 'Hyundai'),
(10, 'Audi'),
(11, 'Subaru'),
(12, 'Lexus'),
(13, 'Mazda');

-- --------------------------------------------------------

--
-- Table structure for table `car_carmodel`
--

CREATE TABLE `car_carmodel` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `make_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `car_carmodel`
--

INSERT INTO `car_carmodel` (`id`, `name`, `make_id`) VALUES
(1, 'RAV4', 1),
(2, 'Fielder', 1),
(3, 'Ranger', 2),
(4, 'Mustang', 2),
(5, 'Civic', 3),
(6, 'Accord', 3),
(7, 'C class', 4),
(8, 'E class', 4),
(9, 'CX-5', 13),
(10, 'CX-9', 13);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-07-25 07:01:56.301763', '1', 'Buses', 1, '[{\"added\": {}}]', 10, 1),
(2, '2023-07-25 07:02:03.095182', '2', 'Double Cabin', 1, '[{\"added\": {}}]', 10, 1),
(3, '2023-07-25 07:02:10.327736', '3', 'Single Cabin', 1, '[{\"added\": {}}]', 10, 1),
(4, '2023-07-25 07:02:18.592552', '4', 'Large SUV', 1, '[{\"added\": {}}]', 10, 1),
(5, '2023-07-25 07:02:40.235585', '5', 'Minivan', 1, '[{\"added\": {}}]', 10, 1),
(6, '2023-07-25 07:03:01.254923', '6', 'Safari 4WD', 1, '[{\"added\": {}}]', 10, 1),
(7, '2023-07-25 07:03:18.798241', '7', 'Saloon', 1, '[{\"added\": {}}]', 10, 1),
(8, '2023-07-25 07:03:27.489751', '8', 'Small SUV', 1, '[{\"added\": {}}]', 10, 1),
(9, '2023-07-25 07:04:42.006091', '3', 'Mazda - CX-5 (2022, Silver, Seats: 4) - YZA901', 2, '[{\"changed\": {\"fields\": [\"Car class\"]}}]', 7, 1),
(10, '2023-07-25 07:05:02.836544', '2', 'Toyota - Fielder (2020, white, Seats: 4) - GHI789', 2, '[{\"changed\": {\"fields\": [\"Car class\"]}}]', 7, 1),
(11, '2023-07-25 07:05:14.877432', '1', 'Toyota - RAV4 (2022, white, Seats: 4) - ABC123', 2, '[{\"changed\": {\"fields\": [\"Car class\"]}}]', 7, 1),
(12, '2023-07-25 10:02:06.126681', '1', 'Toyota - RAV4 (2022, white, Seats: 4) - ABC123', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 7, 1),
(13, '2023-07-25 10:02:18.651496', '1', 'Toyota - RAV4 (2022, white, Seats: 4) - ABC123', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 7, 1),
(14, '2023-07-25 10:06:22.101108', '1', 'Toyota - RAV4 (2022, white, Seats: 4) - ABC123', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 7, 1),
(15, '2023-07-25 10:06:31.899026', '1', 'Toyota - RAV4 (2022, white, Seats: 4) - ABC123', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 7, 1),
(16, '2023-07-25 10:08:56.737461', '1', 'Toyota - RAV4 (2022, white, Seats: 4) - ABC123', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 7, 1),
(17, '2023-07-25 10:09:04.894101', '1', 'Toyota - RAV4 (2022, white, Seats: 4) - ABC123', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 7, 1),
(18, '2023-07-25 10:10:38.170469', '2', 'Toyota - Fielder (2020, white, Seats: 4) - GHI789', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 7, 1),
(19, '2023-07-25 10:10:46.865092', '2', 'Toyota - Fielder (2020, white, Seats: 4) - GHI789', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 7, 1),
(20, '2023-07-25 10:12:47.263827', '3', 'Mazda - CX-5 (2022, Silver, Seats: 4) - YZA901', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 7, 1),
(21, '2023-07-25 10:12:55.466206', '3', 'Mazda - CX-5 (2022, Silver, Seats: 4) - YZA901', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 7, 1),
(22, '2023-07-25 10:41:27.514910', '3', 'Mazda - CX-5 (2022, Silver, Seats: 4) - YZA901', 2, '[{\"changed\": {\"fields\": [\"Weekly rate\", \"Monthly rate\"]}}]', 7, 1),
(23, '2023-07-25 10:41:42.109534', '2', 'Toyota - Fielder (2020, white, Seats: 4) - GHI789', 2, '[{\"changed\": {\"fields\": [\"Weekly rate\", \"Monthly rate\"]}}]', 7, 1),
(24, '2023-07-25 10:41:53.160196', '1', 'Toyota - RAV4 (2022, white, Seats: 4) - ABC123', 2, '[{\"changed\": {\"fields\": [\"Weekly rate\", \"Monthly rate\"]}}]', 7, 1),
(25, '2023-07-27 09:10:17.891694', '8', 'Reservation for Mazda - CX-5 (2022, Silver, Seats: 4) - YZA901 by NELSON MASIBO - nelsonmasibo6@gmail.com (Staff: admin)', 3, '', 12, 1),
(26, '2023-07-27 09:10:17.940481', '7', 'Reservation for Toyota - Fielder (2020, white, Seats: 4) - GHI789 by DAVID KIAMA - david.kiamaa@gmail.com (Staff: admin)', 3, '', 12, 1),
(27, '2023-07-27 09:10:17.982530', '6', 'Reservation for Toyota - Fielder (2020, white, Seats: 4) - GHI789 by NELSON MASIBO - nelsonmasibo6@gmail.com (Staff: admin)', 3, '', 12, 1),
(28, '2023-07-27 09:10:18.015427', '5', 'Reservation for Mazda - CX-5 (2022, Silver, Seats: 4) - YZA901 by kush dinesh - kushdinesh98@gmail.com (Staff: admin)', 3, '', 12, 1),
(29, '2023-07-27 09:10:18.049511', '4', 'Reservation for Toyota - RAV4 (2022, white, Seats: 4) - ABC123 by DAVID KIAMA - david.kiamaa@gmail.com (Staff: admin)', 3, '', 12, 1),
(30, '2023-07-27 09:10:18.148601', '3', 'Reservation for Toyota - RAV4 (2022, white, Seats: 4) - ABC123 by Shynat nganga - shynat@gmail.com (Staff: admin)', 3, '', 12, 1),
(31, '2023-07-27 09:10:18.174230', '2', 'Reservation for Toyota - RAV4 (2022, white, Seats: 4) - ABC123 by Shynat nganga - shynat@gmail.com (Staff: admin)', 3, '', 12, 1),
(32, '2023-07-27 09:10:18.198648', '1', 'Reservation for Toyota - Fielder (2020, white, Seats: 4) - GHI789 by NELSON MASIBO - nelsonmasibo6@gmail.com (Staff: admin)', 3, '', 12, 1),
(33, '2023-07-29 12:16:50.224488', '12', 'Reservation #7101 for Toyota - RAV4 (2022, white, Seats: 4) - ABC123 by DAVID KIAMA - david.kiamaa@gmail.com (Staff: admin)', 3, '', 12, 1),
(34, '2023-07-29 12:16:50.294313', '11', 'Reservation #4169 for Toyota - Fielder (2020, white, Seats: 4) - GHI789 by DAVID KIAMA - david.kiamaa@gmail.com (Staff: admin)', 3, '', 12, 1),
(35, '2023-07-29 12:16:50.327570', '10', 'Reservation #7180 for Toyota - RAV4 (2022, white, Seats: 4) - ABC123 by NELSON MASIBO - nelsonmasibo6@gmail.com (Staff: admin)', 3, '', 12, 1),
(36, '2023-07-29 12:16:50.385281', '9', 'Reservation #None for Toyota - RAV4 (2022, white, Seats: 4) - ABC123 by NELSON MASIBO - nelsonmasibo6@gmail.com (Staff: admin)', 3, '', 12, 1),
(37, '2023-07-31 11:57:07.010096', '17', 'Reservation #0118 for Toyota Fielder - GHI789 by DAVID KIAMA (Staff: admin)', 3, '', 12, 1),
(38, '2023-07-31 11:57:07.072168', '16', 'Reservation #9334 for Toyota Fielder - GHI789 by DAVID KIAMA (Staff: admin)', 3, '', 12, 1),
(39, '2023-07-31 11:57:07.105215', '15', 'Reservation #2313 for Toyota Fielder - GHI789 by NELSON MASIBO (Staff: admin)', 3, '', 12, 1),
(40, '2023-07-31 11:57:07.138101', '14', 'Reservation #2603 for Mazda CX-5 - YZA901 by Shynat nganga (Staff: admin)', 3, '', 12, 1),
(41, '2023-07-31 11:57:07.163706', '13', 'Reservation #0392 for Toyota RAV4 - ABC123 by NELSON MASIBO (Staff: admin)', 3, '', 12, 1),
(42, '2023-07-31 12:21:32.831238', '20', 'Reservation #2215 for Toyota Fielder - GHI789 by NELSON MASIBO (Staff: admin)', 3, '', 12, 1),
(43, '2023-07-31 12:21:32.873020', '19', 'Reservation #1308 for Toyota Fielder - GHI789 by NELSON MASIBO (Staff: admin)', 3, '', 12, 1),
(44, '2023-07-31 12:21:32.906284', '18', 'Reservation #4292 for Toyota Fielder - GHI789 by NELSON MASIBO (Staff: admin)', 3, '', 12, 1),
(45, '2023-07-31 12:52:26.923026', '24', 'Reservation #0935 for Toyota RAV4 - ABC123 by DAVID KIAMA (Staff: admin)', 3, '', 12, 1),
(46, '2023-07-31 12:52:26.970473', '23', 'Reservation #8041 for Mazda CX-5 - YZA901 by DAVID KIAMA (Staff: admin)', 3, '', 12, 1),
(47, '2023-07-31 12:52:26.995859', '22', 'Reservation #5133 for Mazda CX-5 - YZA901 by DAVID KIAMA (Staff: admin)', 3, '', 12, 1),
(48, '2023-07-31 12:52:27.020463', '21', 'Reservation #2594 for Toyota Fielder - GHI789 by NELSON MASIBO (Staff: admin)', 3, '', 12, 1),
(49, '2023-07-31 12:54:52.947443', '26', 'Reservation #5939 for Toyota RAV4 - ABC123 by NELSON MASIBO (Staff: admin)', 3, '', 12, 1),
(50, '2023-07-31 12:54:53.024356', '25', 'Reservation #7959 for Toyota RAV4 - ABC123 by DAVID KIAMA (Staff: admin)', 3, '', 12, 1),
(51, '2023-07-31 12:56:35.484452', '27', 'Reservation #2702 for Toyota RAV4 - ABC123 by NELSON MASIBO (Staff: admin)', 3, '', 12, 1),
(52, '2023-07-31 12:59:03.675331', '28', 'Reservation #9530 for Toyota RAV4 - ABC123 by NELSON MASIBO (Staff: admin)', 3, '', 12, 1),
(53, '2023-08-11 08:02:39.819020', '1', 'Toyota RAV4 - ABC123', 3, '', 15, 1),
(54, '2023-08-11 08:02:50.414972', '30', 'Reservation #7812 for Toyota RAV4 - ABC123 by NELSON MASIBO (Staff: Nelson)', 3, '', 12, 1),
(55, '2023-08-11 08:02:50.480513', '29', 'Reservation #2648 for Toyota RAV4 - ABC123 by NELSON MASIBO (Staff: admin)', 3, '', 12, 1),
(56, '2023-08-11 08:05:07.494140', '4', 'Toyota RAV4 - ABC123', 3, '', 15, 1),
(57, '2023-08-11 08:05:07.560460', '3', 'Toyota RAV4 - ABC123', 3, '', 15, 1),
(58, '2023-08-11 08:05:07.593420', '2', 'Toyota RAV4 - ABC123', 3, '', 15, 1),
(59, '2023-08-11 08:19:14.576739', '5', 'Toyota RAV4 - ABC123', 3, '', 15, 1),
(60, '2023-08-11 08:19:32.329847', '32', 'Reservation #8699 for Toyota Fielder - GHI789 by NELSON MASIBO (Staff: Nelson)', 3, '', 12, 1),
(61, '2023-08-11 08:19:32.381874', '31', 'Reservation #7703 for Toyota RAV4 - ABC123 by NELSON MASIBO (Staff: Nelson)', 3, '', 12, 1),
(62, '2023-08-11 08:31:43.236670', '7', 'Toyota RAV4 - ABC123', 3, '', 15, 1),
(63, '2023-08-11 08:31:43.282765', '6', 'Toyota RAV4 - ABC123', 3, '', 15, 1),
(64, '2023-08-11 09:44:28.884727', '1', 'Cash', 1, '[{\"added\": {}}]', 16, 1),
(65, '2023-08-11 09:44:37.090307', '2', 'M-pesa', 1, '[{\"added\": {}}]', 16, 1),
(66, '2023-08-11 09:44:41.560673', '3', 'Card', 1, '[{\"added\": {}}]', 16, 1),
(67, '2023-08-11 12:32:49.266349', '1', 'ISN.PSV.R/L.INSP', 1, '[{\"added\": {}}]', 18, 1),
(68, '2023-08-11 12:32:56.462099', '2', 'CD PLAYER', 1, '[{\"added\": {}}]', 18, 1),
(69, '2023-08-11 12:33:13.031086', '3', 'REAR', 1, '[{\"added\": {}}]', 18, 1),
(70, '2023-08-11 12:33:16.110998', '4', 'FRONT', 1, '[{\"added\": {}}]', 18, 1),
(71, '2023-08-11 12:33:31.834623', '5', 'SPEAKER', 1, '[{\"added\": {}}]', 18, 1),
(72, '2023-08-11 12:33:51.165267', '6', 'FLOOR MATS', 1, '[{\"added\": {}}]', 18, 1),
(73, '2023-08-11 12:33:55.882480', '7', 'REAR LEFT', 1, '[{\"added\": {}}]', 18, 1),
(74, '2023-08-11 12:33:59.822229', '8', 'REAR RIGHT', 1, '[{\"added\": {}}]', 18, 1),
(75, '2023-08-11 12:34:08.938271', '9', 'FRONT LEFT', 1, '[{\"added\": {}}]', 18, 1),
(76, '2023-08-11 12:34:12.889020', '10', 'FRONT RIGHT', 1, '[{\"added\": {}}]', 18, 1),
(77, '2023-08-11 12:34:20.030820', '11', 'WHEEL CAP', 1, '[{\"added\": {}}]', 18, 1),
(78, '2023-08-11 12:34:29.755398', '12', 'REAR LEFT', 1, '[{\"added\": {}}]', 18, 1),
(79, '2023-08-11 12:34:37.056602', '13', 'REAR RIGHT', 1, '[{\"added\": {}}]', 18, 1),
(80, '2023-08-11 12:34:43.789883', '14', 'FRONT LEFT', 1, '[{\"added\": {}}]', 18, 1),
(81, '2023-08-11 12:35:44.085589', '15', 'FRONT RIGHT', 1, '[{\"added\": {}}]', 18, 1),
(82, '2023-08-11 12:35:48.872458', '16', 'WINDOWS', 1, '[{\"added\": {}}]', 18, 1),
(83, '2023-08-11 12:35:56.037238', '17', 'RADIOTOR CAP', 1, '[{\"added\": {}}]', 18, 1),
(84, '2023-08-11 12:36:00.585510', '18', 'WATER CAP', 1, '[{\"added\": {}}]', 18, 1),
(85, '2023-08-11 12:36:05.852071', '19', 'OIL CAP', 1, '[{\"added\": {}}]', 18, 1),
(86, '2023-08-11 12:36:13.005288', '20', 'ENGINE', 1, '[{\"added\": {}}]', 18, 1),
(87, '2023-08-11 12:36:17.099449', '21', 'REAR LEFT', 1, '[{\"added\": {}}]', 18, 1),
(88, '2023-08-11 12:36:23.438205', '22', 'REAR LEFT', 1, '[{\"added\": {}}]', 18, 1),
(89, '2023-08-11 12:36:32.309141', '23', 'REAR RIGHT', 1, '[{\"added\": {}}]', 18, 1),
(90, '2023-08-11 12:37:05.150099', '24', 'FRONT LEFT', 1, '[{\"added\": {}}]', 18, 1),
(91, '2023-08-11 12:37:09.066420', '25', 'FRONT RIGHT', 1, '[{\"added\": {}}]', 18, 1),
(92, '2023-08-11 12:37:15.225711', '26', 'MUD GUARDS', 1, '[{\"added\": {}}]', 18, 1),
(93, '2023-08-11 12:37:22.095758', '27', 'REAR WIND SCREEN', 1, '[{\"added\": {}}]', 18, 1),
(94, '2023-08-11 12:37:30.324064', '28', 'FRONT WIND SCREEN', 1, '[{\"added\": {}}]', 18, 1),
(95, '2023-08-11 12:37:42.445997', '29', 'SPEEDO SEAL', 1, '[{\"added\": {}}]', 18, 1),
(96, '2023-08-11 12:37:50.623629', '30', 'TAPE/RADIO', 1, '[{\"added\": {}}]', 18, 1),
(97, '2023-08-11 12:38:02.230037', '31', 'SPARE WHEEL', 1, '[{\"added\": {}}]', 18, 1),
(98, '2023-08-11 12:38:07.004310', '32', 'W/SPANNER', 1, '[{\"added\": {}}]', 18, 1),
(99, '2023-08-11 12:38:16.189593', '33', 'JACK', 1, '[{\"added\": {}}]', 18, 1),
(100, '2023-08-11 12:38:20.830537', '34', 'SPARE WHEEL', 1, '[{\"added\": {}}]', 18, 1),
(101, '2023-08-11 12:42:08.599892', '1', 'CarInspection object (1)', 1, '[{\"added\": {}}]', 19, 1),
(102, '2023-08-11 12:42:32.685808', '1', 'InspectionItemStatus object (1)', 1, '[{\"added\": {}}]', 17, 1),
(103, '2023-08-11 13:50:51.849636', '35', 'InspectionItemStatus object (35)', 2, '[{\"changed\": {\"fields\": [\"Checked out\"]}}]', 17, 1),
(104, '2023-08-11 14:56:42.517910', '35', 'CarInspection object (2) - SPARE WHEEL', 3, '', 17, 1),
(105, '2023-08-11 14:56:42.551887', '34', 'CarInspection object (2) - JACK', 3, '', 17, 1),
(106, '2023-08-11 14:56:42.568878', '33', 'CarInspection object (2) - W/SPANNER', 3, '', 17, 1),
(107, '2023-08-11 14:56:42.593635', '32', 'CarInspection object (2) - SPARE WHEEL', 3, '', 17, 1),
(108, '2023-08-11 14:56:42.610979', '31', 'CarInspection object (2) - TAPE/RADIO', 3, '', 17, 1),
(109, '2023-08-11 14:56:42.635680', '30', 'CarInspection object (2) - SPEEDO SEAL', 3, '', 17, 1),
(110, '2023-08-11 14:56:42.669220', '29', 'CarInspection object (2) - FRONT WIND SCREEN', 3, '', 17, 1),
(111, '2023-08-11 14:56:42.802506', '28', 'CarInspection object (2) - REAR WIND SCREEN', 3, '', 17, 1),
(112, '2023-08-11 14:56:42.827024', '27', 'CarInspection object (2) - MUD GUARDS', 3, '', 17, 1),
(113, '2023-08-11 14:56:42.852424', '26', 'CarInspection object (2) - FRONT RIGHT', 3, '', 17, 1),
(114, '2023-08-11 14:56:42.877033', '25', 'CarInspection object (2) - FRONT LEFT', 3, '', 17, 1),
(115, '2023-08-11 14:56:42.902475', '24', 'CarInspection object (2) - REAR RIGHT', 3, '', 17, 1),
(116, '2023-08-11 14:56:42.960751', '23', 'CarInspection object (2) - REAR LEFT', 3, '', 17, 1),
(117, '2023-08-11 14:56:42.985796', '22', 'CarInspection object (2) - REAR LEFT', 3, '', 17, 1),
(118, '2023-08-11 14:56:43.010806', '21', 'CarInspection object (2) - ENGINE', 3, '', 17, 1),
(119, '2023-08-11 14:56:43.036309', '20', 'CarInspection object (2) - OIL CAP', 3, '', 17, 1),
(120, '2023-08-11 14:56:43.060410', '19', 'CarInspection object (2) - WATER CAP', 3, '', 17, 1),
(121, '2023-08-11 14:56:43.085821', '18', 'CarInspection object (2) - RADIOTOR CAP', 3, '', 17, 1),
(122, '2023-08-11 14:56:43.277442', '17', 'CarInspection object (2) - WINDOWS', 3, '', 17, 1),
(123, '2023-08-11 14:56:43.377454', '16', 'CarInspection object (2) - FRONT RIGHT', 3, '', 17, 1),
(124, '2023-08-11 14:56:43.411493', '15', 'CarInspection object (2) - FRONT LEFT', 3, '', 17, 1),
(125, '2023-08-11 14:56:43.460339', '14', 'CarInspection object (2) - REAR RIGHT', 3, '', 17, 1),
(126, '2023-08-11 14:56:43.502665', '13', 'CarInspection object (2) - REAR LEFT', 3, '', 17, 1),
(127, '2023-08-11 14:56:43.527462', '12', 'CarInspection object (2) - WHEEL CAP', 3, '', 17, 1),
(128, '2023-08-11 14:56:43.560812', '11', 'CarInspection object (2) - FRONT RIGHT', 3, '', 17, 1),
(129, '2023-08-11 14:56:43.585596', '10', 'CarInspection object (2) - FRONT LEFT', 3, '', 17, 1),
(130, '2023-08-11 14:56:43.611598', '9', 'CarInspection object (2) - REAR RIGHT', 3, '', 17, 1),
(131, '2023-08-11 14:56:43.652571', '8', 'CarInspection object (2) - REAR LEFT', 3, '', 17, 1),
(132, '2023-08-11 14:56:43.677565', '7', 'CarInspection object (2) - FLOOR MATS', 3, '', 17, 1),
(133, '2023-08-11 14:56:43.729977', '6', 'CarInspection object (2) - SPEAKER', 3, '', 17, 1),
(134, '2023-08-11 14:56:43.777722', '5', 'CarInspection object (2) - FRONT', 3, '', 17, 1),
(135, '2023-08-11 14:56:43.827354', '4', 'CarInspection object (2) - REAR', 3, '', 17, 1),
(136, '2023-08-11 14:56:43.852717', '3', 'CarInspection object (2) - CD PLAYER', 3, '', 17, 1),
(137, '2023-08-11 14:56:43.877200', '2', 'CarInspection object (2) - ISN.PSV.R/L.INSP', 3, '', 17, 1),
(138, '2023-08-11 14:56:43.902724', '1', 'CarInspection object (1) - ISN.PSV.R/L.INSP', 3, '', 17, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(7, 'car', 'car'),
(10, 'car', 'carclass'),
(9, 'car', 'carmake'),
(8, 'car', 'carmodel'),
(4, 'contenttypes', 'contenttype'),
(19, 'reservations', 'carinspection'),
(15, 'reservations', 'carout'),
(20, 'reservations', 'fuel'),
(18, 'reservations', 'inspectionitem'),
(17, 'reservations', 'inspectionitemstatus'),
(16, 'reservations', 'paymentmethod'),
(12, 'reservations', 'reservation'),
(14, 'reservations', 'taxes'),
(5, 'sessions', 'session'),
(11, 'users', 'client'),
(6, 'users', 'customuser'),
(13, 'users', 'driver');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-07-24 17:50:11.885250'),
(2, 'contenttypes', '0002_remove_content_type_name', '2023-07-24 17:50:11.981665'),
(3, 'auth', '0001_initial', '2023-07-24 17:50:12.237696'),
(4, 'auth', '0002_alter_permission_name_max_length', '2023-07-24 17:50:12.319953'),
(5, 'auth', '0003_alter_user_email_max_length', '2023-07-24 17:50:12.328946'),
(6, 'auth', '0004_alter_user_username_opts', '2023-07-24 17:50:12.340943'),
(7, 'auth', '0005_alter_user_last_login_null', '2023-07-24 17:50:12.348936'),
(8, 'auth', '0006_require_contenttypes_0002', '2023-07-24 17:50:12.352938'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2023-07-24 17:50:12.362931'),
(10, 'auth', '0008_alter_user_username_max_length', '2023-07-24 17:50:12.374921'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2023-07-24 17:50:12.388926'),
(12, 'auth', '0010_alter_group_name_max_length', '2023-07-24 17:50:12.425891'),
(13, 'auth', '0011_update_proxy_permissions', '2023-07-24 17:50:12.436840'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2023-07-24 17:50:12.446832'),
(15, 'users', '0001_initial', '2023-07-24 17:50:12.799714'),
(16, 'admin', '0001_initial', '2023-07-24 17:50:12.946988'),
(17, 'admin', '0002_logentry_remove_auto_add', '2023-07-24 17:50:12.957246'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2023-07-24 17:50:12.972763'),
(19, 'car', '0001_initial', '2023-07-24 17:50:13.033727'),
(20, 'car', '0002_delete_carmodel', '2023-07-24 17:50:13.046003'),
(21, 'car', '0003_carmodel_remove_car_make_alter_car_model', '2023-07-24 17:50:13.230757'),
(22, 'car', '0004_alter_car_year', '2023-07-24 17:50:18.772007'),
(23, 'car', '0005_alter_car_year', '2023-07-24 17:50:18.915777'),
(24, 'car', '0006_remove_car_available_units', '2023-07-24 17:50:18.955360'),
(25, 'sessions', '0001_initial', '2023-07-24 17:50:19.013382'),
(26, 'car', '0007_carmake_remove_car_name_carmodel_make', '2023-07-24 18:10:36.137992'),
(27, 'car', '0008_car_make', '2023-07-24 18:54:50.017179'),
(28, 'car', '0009_carclass_car_car_class', '2023-07-25 06:49:03.492149'),
(29, 'users', '0002_client', '2023-07-25 07:27:01.196607'),
(30, 'users', '0003_alter_client_phone_number', '2023-07-25 08:25:14.080994'),
(31, 'car', '0010_car_monthly_rate_car_weekly_rate', '2023-07-25 10:37:02.704328'),
(32, 'reservations', '0001_initial', '2023-07-25 11:07:08.204295'),
(33, 'reservations', '0002_alter_reservation_discount', '2023-07-25 13:22:14.746894'),
(34, 'reservations', '0003_reservation_created_at', '2023-07-26 07:00:12.977555'),
(35, 'reservations', '0004_alter_reservation_created_at', '2023-07-26 07:00:13.172495'),
(36, 'reservations', '0005_reservation_days_reservation_rates_applied', '2023-07-27 08:33:34.028225'),
(37, 'reservations', '0006_reservation_reservation_number', '2023-07-28 06:52:00.488211'),
(38, 'car', '0011_car_mileage', '2023-07-31 11:01:28.359368'),
(39, 'reservations', '0007_taxes', '2023-07-31 11:01:28.523962'),
(40, 'reservations', '0008_reservation_vat', '2023-07-31 11:01:28.672333'),
(41, 'reservations', '0009_remove_reservation_vat_alter_reservation_end_date_and_more', '2023-07-31 11:01:30.256196'),
(42, 'reservations', '0010_reservation_add_tax_reservation_use_custom_rates', '2023-07-31 11:01:30.725424'),
(43, 'reservations', '0011_remove_reservation_discount', '2023-07-31 11:01:30.973791'),
(44, 'reservations', '0012_rename_add_tax_reservation_add_vat_and_more', '2023-07-31 11:01:31.133753'),
(45, 'reservations', '0013_rename_rates_applied_reservation_daily_rates', '2023-07-31 11:01:31.248747'),
(46, 'reservations', '0014_rename_rate_reservation_total_amount_and_more', '2023-07-31 11:01:31.507589'),
(47, 'users', '0004_driver_client_company_client_country_and_more', '2023-07-31 11:01:32.034782'),
(48, 'reservations', '0015_carout_alter_reservation_total_amount', '2023-07-31 13:55:48.770452'),
(49, 'car', '0012_alter_car_model', '2023-07-31 14:14:57.752146'),
(50, 'reservations', '0016_carout_age_carout_card_expiry_and_more', '2023-08-11 07:42:33.247625'),
(51, 'reservations', '0017_alter_carout_physical_address_and_more', '2023-08-11 07:42:35.527701'),
(52, 'users', '0005_remove_client_country_client_age_client_card_expiry_and_more', '2023-08-11 07:42:52.013633'),
(53, 'reservations', '0018_alter_carout_number_plate', '2023-08-11 08:04:30.397187'),
(54, 'reservations', '0019_carout_email_carout_id_number', '2023-08-11 09:04:59.417072'),
(55, 'reservations', '0020_carout_where_the_car_will_be_used_or_parked', '2023-08-11 09:34:59.720477'),
(56, 'reservations', '0021_paymentmethod', '2023-08-11 09:44:16.836589'),
(57, 'reservations', '0022_carout_amount_carout_deposit_carout_payment_method', '2023-08-11 09:50:32.280032'),
(58, 'reservations', '0023_carinspection_inspectionitem_inspectionitemstatus_and_more', '2023-08-11 12:31:19.657391'),
(59, 'reservations', '0024_fuel_inspectionitemstatus_damages_noted_and_more', '2023-08-11 14:33:29.889567');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('799lmqv1sz632wzc3asycyb5rsiagixf', '.eJxVizsOwjAQBe_iGkXY3l1sSiTOYT3HazniU2BSIe6eREoB5byZ9zEJ87uluesrTcWcjTWH3y1jvOlzExv2Yec-XB-Y7pfd_l0aelt7BJbIxEXFU60nH4QhhNGWDKZcmaDsIMHGowqQQTlwLCJO2TvzXQCMwDKS:1qP2BO:JsXvbHT9evC2QPMpgIV57gl9Cam-6-UepF0FA5qbdNM', '2023-08-10 14:41:38.473296'),
('bcg7aiws0htua6skh9c243b787fgk0fz', '.eJxVizsOwjAQBe_iGkXY3l1sSiTOYT3HazniU2BSIe6eREoB5byZ9zEJ87uluesrTcWcjTWH3y1jvOlzExv2Yec-XB-Y7pfd_l0aelt7BJbIxEXFU60nH4QhhNGWDKZcmaDsIMHGowqQQTlwLCJO2TvzXQCMwDKS:1qP1G7:9doQuLZ1bCJmf6XY2yrK-usiGABietxg5ieBZnT4koE', '2023-08-10 13:42:27.158949'),
('dgwwixmj0syxe6l8n7i6wtbz1sqglxvs', '.eJxVizsOwjAQBe_iGkXY3l1sSiTOYT3HazniU2BSIe6eREoB5byZ9zEJ87uluesrTcWcjTWH3y1jvOlzExv2Yec-XB-Y7pfd_l0aelt7BJbIxEXFU60nH4QhhNGWDKZcmaDsIMHGowqQQTlwLCJO2TvzXQCMwDKS:1qOIcU:t3YqGkabJVmz9H_CJgPoU83TK6HI-h49ub6zTElraj4', '2023-08-08 14:02:34.215784'),
('g9262voxa1hrbsav8kklyn162arlxsle', '.eJxVi0sOwjAMBe-SNarkOEljlkicI3JcW6n4LAhdIe5OK3VBlzPz3scVXt6tLF1fZZ7c2Xl3-neV5abPLWzYh537cH3wfL_s9XBp3Nu6V6RQAdCYcqAIrDHmiKpmSTLqmCEYJ_AGSl6SBQ9VRl6lChK47w-KeTLJ:1qUN3S:U8kjYiboCcNJSUF2v5lCjJfQyHTJbud6fESDELyfCnc', '2023-08-25 07:59:30.875342'),
('nastj4a1hd4tgq69ftvwjy3i8gqpfrhm', '.eJxVizsOwjAQBe_iGkXY3l1sSiTOYT3HazniU2BSIe6eREoB5byZ9zEJ87uluesrTcWcjTWH3y1jvOlzExv2Yec-XB-Y7pfd_l0aelt7BJbIxEXFU60nH4QhhNGWDKZcmaDsIMHGowqQQTlwLCJO2TvzXQCMwDKS:1qOvjg:O4tOJT_16Joi2KJZnnWtXvA2MN-nqE8ZTmc7EhAnFas', '2023-08-10 07:48:36.306760'),
('pofeabbop8zdtszho9t214nfa80w8rrg', '.eJxVizsOwjAQBe_iGkXY3l1sSiTOYT3HazniU2BSIe6eREoB5byZ9zEJ87uluesrTcWcjTWH3y1jvOlzExv2Yec-XB-Y7pfd_l0aelt7BJbIxEXFU60nH4QhhNGWDKZcmaDsIMHGowqQQTlwLCJO2TvzXQCMwDKS:1qPisC:F3Gy2eeVDYQjI-H1vsUMNiPxwWDgNxlkXgbiNj1hMYw', '2023-08-12 12:16:40.503490'),
('vqt4ecny09rhdjw5s9d07g6z6gr4x4y7', '.eJxVizsOwjAQBe_iGkXY3l1sSiTOYT3HazniU2BSIe6eREoB5byZ9zEJ87uluesrTcWcjTWH3y1jvOlzExv2Yec-XB-Y7pfd_l0aelt7BJbIxEXFU60nH4QhhNGWDKZcmaDsIMHGowqQQTlwLCJO2TvzXQCMwDKS:1qUN2T:l17Z9BsNym-Ej27nAw5lO5i85-KgiQddKfZEJ1uI7e0', '2023-08-25 07:58:29.885375'),
('w8q4f28rwtec8q8idxaz4xxmmfp3fm73', '.eJxVizsOwjAQBe_iGkXY3l1sSiTOYT3HazniU2BSIe6eREoB5byZ9zEJ87uluesrTcWcjTWH3y1jvOlzExv2Yec-XB-Y7pfd_l0aelt7BJbIxEXFU60nH4QhhNGWDKZcmaDsIMHGowqQQTlwLCJO2TvzXQCMwDKS:1qOwYQ:T85bRpgklnO35fEAJCImPqtEFShSezELCTCly7uZkB8', '2023-08-10 08:41:02.387273'),
('xi5uei6q84cari81ynvlips29akh9pqv', '.eJxVizsOwjAQBe_iGkXY3l1sSiTOYT3HazniU2BSIe6eREoB5byZ9zEJ87uluesrTcWcjTWH3y1jvOlzExv2Yec-XB-Y7pfd_l0aelt7BJbIxEXFU60nH4QhhNGWDKZcmaDsIMHGowqQQTlwLCJO2TvzXQCMwDKS:1qOC03:Shwzr5M1nipzfmYASjP2nV4DHiphu72vnoA3BLyyNvU', '2023-08-08 06:58:27.189679');

-- --------------------------------------------------------

--
-- Table structure for table `reservations_carinspection`
--

CREATE TABLE `reservations_carinspection` (
  `id` bigint(20) NOT NULL,
  `inspection_date` datetime(6) NOT NULL,
  `car_out_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reservations_carinspection`
--

INSERT INTO `reservations_carinspection` (`id`, `inspection_date`, `car_out_id`) VALUES
(1, '2023-08-11 12:42:08.590847', 8),
(2, '2023-08-11 13:42:01.970969', 9),
(3, '2023-08-11 15:08:49.049998', 10);

-- --------------------------------------------------------

--
-- Table structure for table `reservations_carout`
--

CREATE TABLE `reservations_carout` (
  `id` bigint(20) NOT NULL,
  `number_plate` varchar(20) NOT NULL,
  `make` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  `year` int(10) UNSIGNED NOT NULL CHECK (`year` >= 0),
  `color` varchar(50) NOT NULL,
  `daily_rate` decimal(8,2) NOT NULL,
  `seating_capacity` int(10) UNSIGNED NOT NULL CHECK (`seating_capacity` >= 0),
  `car_class` varchar(100) NOT NULL,
  `mileage` int(10) UNSIGNED NOT NULL CHECK (`mileage` >= 0),
  `age` int(10) UNSIGNED DEFAULT NULL CHECK (`age` >= 0),
  `card_expiry` date DEFAULT NULL,
  `country_of_issue` varchar(50) DEFAULT NULL,
  `credit_card` varchar(50) DEFAULT NULL,
  `credit_card_number` varchar(16) DEFAULT NULL,
  `drivers_license_number` varchar(50) DEFAULT NULL,
  `full_name` varchar(150) DEFAULT NULL,
  `ld_appt_number` varchar(50) DEFAULT NULL,
  `license_expiry` date DEFAULT NULL,
  `mobile_number` varchar(20) DEFAULT NULL,
  `nationality` varchar(50) DEFAULT NULL,
  `office_telephone` varchar(20) DEFAULT NULL,
  `physical_address` varchar(100) DEFAULT NULL,
  `residence_address` varchar(100) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `id_number` varchar(20) DEFAULT NULL,
  `where_the_car_will_be_used_or_parked` varchar(100) DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `deposit` decimal(10,2) DEFAULT NULL,
  `payment_method_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reservations_carout`
--

INSERT INTO `reservations_carout` (`id`, `number_plate`, `make`, `model`, `year`, `color`, `daily_rate`, `seating_capacity`, `car_class`, `mileage`, `age`, `card_expiry`, `country_of_issue`, `credit_card`, `credit_card_number`, `drivers_license_number`, `full_name`, `ld_appt_number`, `license_expiry`, `mobile_number`, `nationality`, `office_telephone`, `physical_address`, `residence_address`, `email`, `id_number`, `where_the_car_will_be_used_or_parked`, `amount`, `deposit`, `payment_method_id`) VALUES
(8, 'ABC123', 'Toyota', 'RAV4', 2022, 'white', 30.00, 4, 'Small SUV', 0, NULL, NULL, NULL, NULL, NULL, NULL, 'DAVID KIAMA', '454556', NULL, '+254722921960', NULL, NULL, NULL, NULL, 'david.kiamaa@gmail.com', '35100087', 'rtty', 104.40, 50.00, 3),
(9, 'YZA901', 'Mazda', 'CX-5', 2022, 'Silver', 45.00, 4, 'Large SUV', 0, NULL, NULL, NULL, NULL, NULL, NULL, 'Shynat nganga', '454556', NULL, '0704122213', NULL, NULL, NULL, NULL, 'shynat@gmail.com', '35100088', 'rttytty', 156.60, 50.00, 3),
(10, 'GHI789', 'Toyota', 'Fielder', 2020, 'white', 30.00, 4, 'Small SUV', 0, NULL, NULL, NULL, NULL, NULL, NULL, 'kush dinesh', NULL, NULL, '0704122214', NULL, NULL, NULL, NULL, 'kushdinesh98@gmail.com', '35100089', NULL, 69.60, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `reservations_fuel`
--

CREATE TABLE `reservations_fuel` (
  `id` bigint(20) NOT NULL,
  `level` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `reservations_inspectionitem`
--

CREATE TABLE `reservations_inspectionitem` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reservations_inspectionitem`
--

INSERT INTO `reservations_inspectionitem` (`id`, `name`) VALUES
(1, 'ISN.PSV.R/L.INSP'),
(2, 'CD PLAYER'),
(3, 'REAR'),
(4, 'FRONT'),
(5, 'SPEAKER'),
(6, 'FLOOR MATS'),
(7, 'REAR LEFT'),
(8, 'REAR RIGHT'),
(9, 'FRONT LEFT'),
(10, 'FRONT RIGHT'),
(11, 'WHEEL CAP'),
(12, 'REAR LEFT'),
(13, 'REAR RIGHT'),
(14, 'FRONT LEFT'),
(15, 'FRONT RIGHT'),
(16, 'WINDOWS'),
(17, 'RADIOTOR CAP'),
(18, 'WATER CAP'),
(19, 'OIL CAP'),
(20, 'ENGINE'),
(21, 'REAR LEFT'),
(22, 'REAR LEFT'),
(23, 'REAR RIGHT'),
(24, 'FRONT LEFT'),
(25, 'FRONT RIGHT'),
(26, 'MUD GUARDS'),
(27, 'REAR WIND SCREEN'),
(28, 'FRONT WIND SCREEN'),
(29, 'SPEEDO SEAL'),
(30, 'TAPE/RADIO'),
(31, 'SPARE WHEEL'),
(32, 'W/SPANNER'),
(33, 'JACK'),
(34, 'SPARE WHEEL');

-- --------------------------------------------------------

--
-- Table structure for table `reservations_inspectionitemstatus`
--

CREATE TABLE `reservations_inspectionitemstatus` (
  `id` bigint(20) NOT NULL,
  `checked_out` tinyint(1) NOT NULL,
  `checked_in` tinyint(1) NOT NULL,
  `car_inspection_id` bigint(20) NOT NULL,
  `inspection_item_id` bigint(20) NOT NULL,
  `damages_noted` longtext DEFAULT NULL,
  `kms_allowed` int(10) UNSIGNED DEFAULT NULL CHECK (`kms_allowed` >= 0),
  `kms_driven` int(10) UNSIGNED DEFAULT NULL CHECK (`kms_driven` >= 0),
  `kms_in` int(10) UNSIGNED DEFAULT NULL CHECK (`kms_in` >= 0),
  `kms_out` int(10) UNSIGNED DEFAULT NULL CHECK (`kms_out` >= 0),
  `fuel_in_id` bigint(20) DEFAULT NULL,
  `fuel_out_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reservations_inspectionitemstatus`
--

INSERT INTO `reservations_inspectionitemstatus` (`id`, `checked_out`, `checked_in`, `car_inspection_id`, `inspection_item_id`, `damages_noted`, `kms_allowed`, `kms_driven`, `kms_in`, `kms_out`, `fuel_in_id`, `fuel_out_id`) VALUES
(36, 1, 0, 3, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(37, 0, 0, 3, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(38, 0, 0, 3, 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(39, 0, 0, 3, 4, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(40, 1, 0, 3, 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(41, 0, 0, 3, 6, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(42, 0, 0, 3, 7, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(43, 0, 0, 3, 8, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(44, 1, 0, 3, 9, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(45, 0, 0, 3, 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(46, 0, 0, 3, 11, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(47, 0, 0, 3, 12, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(48, 1, 0, 3, 13, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(49, 0, 0, 3, 14, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(50, 0, 0, 3, 15, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(51, 0, 0, 3, 16, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(52, 0, 0, 3, 17, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(53, 1, 0, 3, 18, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(54, 0, 0, 3, 19, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(55, 0, 0, 3, 20, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(56, 0, 0, 3, 21, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(57, 1, 0, 3, 22, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(58, 1, 0, 3, 23, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(59, 0, 0, 3, 24, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(60, 0, 0, 3, 25, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(61, 1, 0, 3, 26, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(62, 1, 0, 3, 27, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(63, 0, 0, 3, 28, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(64, 0, 0, 3, 29, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(65, 1, 0, 3, 30, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(66, 0, 0, 3, 31, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(67, 0, 0, 3, 32, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(68, 0, 0, 3, 33, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(69, 0, 0, 3, 34, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `reservations_paymentmethod`
--

CREATE TABLE `reservations_paymentmethod` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reservations_paymentmethod`
--

INSERT INTO `reservations_paymentmethod` (`id`, `name`) VALUES
(3, 'Card'),
(1, 'Cash'),
(2, 'M-pesa');

-- --------------------------------------------------------

--
-- Table structure for table `reservations_reservation`
--

CREATE TABLE `reservations_reservation` (
  `id` bigint(20) NOT NULL,
  `start_date` datetime(6) NOT NULL,
  `end_date` datetime(6) NOT NULL,
  `total_amount` decimal(8,2) DEFAULT NULL,
  `car_id` bigint(20) NOT NULL,
  `client_id` bigint(20) NOT NULL,
  `staff_id` bigint(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `days` int(10) UNSIGNED DEFAULT NULL CHECK (`days` >= 0),
  `daily_rates` decimal(8,2) DEFAULT NULL,
  `reservation_number` varchar(20) DEFAULT NULL,
  `add_VAT` tinyint(1) NOT NULL,
  `apply_normal_rates` tinyint(1) NOT NULL,
  `total_amount_vat` decimal(8,2) DEFAULT NULL,
  `vat` decimal(8,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reservations_reservation`
--

INSERT INTO `reservations_reservation` (`id`, `start_date`, `end_date`, `total_amount`, `car_id`, `client_id`, `staff_id`, `created_at`, `days`, `daily_rates`, `reservation_number`, `add_VAT`, `apply_normal_rates`, `total_amount_vat`, `vat`) VALUES
(33, '2023-08-12 08:19:00.000000', '2023-08-13 08:19:00.000000', 60.00, 1, 1, 2, '2023-08-11 08:19:51.105733', 2, 30.00, '4877', 1, 1, 69.60, 9.60),
(34, '2023-08-19 08:37:00.000000', '2023-08-21 08:37:00.000000', 90.00, 2, 2, 2, '2023-08-11 08:37:59.795308', 3, 30.00, '4823', 1, 1, 104.40, 14.40),
(35, '2023-08-19 09:13:00.000000', '2023-08-21 09:13:00.000000', 90.00, 1, 2, 2, '2023-08-11 09:13:31.950919', 3, 30.00, '6591', 1, 1, 104.40, 14.40),
(36, '2023-08-17 12:58:00.000000', '2023-08-19 12:58:00.000000', 135.00, 3, 3, 2, '2023-08-11 12:58:25.107460', 3, 45.00, '8931', 1, 1, 156.60, 21.60),
(37, '2023-08-22 15:01:00.000000', '2023-08-23 15:01:00.000000', 60.00, 2, 4, 2, '2023-08-11 15:02:00.838311', 2, 30.00, '4774', 1, 1, 69.60, 9.60);

-- --------------------------------------------------------

--
-- Table structure for table `reservations_taxes`
--

CREATE TABLE `reservations_taxes` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `rate` decimal(8,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users_client`
--

CREATE TABLE `users_client` (
  `id` bigint(20) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `id_number` varchar(20) NOT NULL,
  `company` varchar(100) DEFAULT NULL,
  `home_address` varchar(255) DEFAULT NULL,
  `local_address` varchar(255) DEFAULT NULL,
  `age` int(10) UNSIGNED DEFAULT NULL CHECK (`age` >= 0),
  `card_expiry` date DEFAULT NULL,
  `country_of_issue` varchar(50) DEFAULT NULL,
  `credit_card` varchar(50) DEFAULT NULL,
  `credit_card_number` varchar(16) DEFAULT NULL,
  `drivers_license_number` varchar(50) DEFAULT NULL,
  `license_expiry` date DEFAULT NULL,
  `nationality` varchar(50) DEFAULT NULL,
  `office_telephone` varchar(20) DEFAULT NULL,
  `physical_address` longtext DEFAULT NULL,
  `residence_address` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users_client`
--

INSERT INTO `users_client` (`id`, `first_name`, `last_name`, `email`, `phone_number`, `id_number`, `company`, `home_address`, `local_address`, `age`, `card_expiry`, `country_of_issue`, `credit_card`, `credit_card_number`, `drivers_license_number`, `license_expiry`, `nationality`, `office_telephone`, `physical_address`, `residence_address`) VALUES
(1, 'NELSON', 'MASIBO', 'nelsonmasibo6@gmail.com', '0704122212', '35100086', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, 'DAVID', 'KIAMA', 'david.kiamaa@gmail.com', '+254722921960', '35100087', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(3, 'Shynat', 'nganga', 'shynat@gmail.com', '0704122213', '35100088', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(4, 'kush', 'dinesh', 'kushdinesh98@gmail.com', '0704122214', '35100089', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users_customuser`
--

CREATE TABLE `users_customuser` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `email` varchar(254) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users_customuser`
--

INSERT INTO `users_customuser` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `is_staff`, `is_active`, `date_joined`, `email`) VALUES
(1, 'pbkdf2_sha256$600000$frBFQjr3Sua0MF4HmyFBAg$We/sB3ciIves35JgonQkAwae0QEDXPb//ddpCOrdRbo=', '2023-08-11 07:58:29.810421', 1, 'admin', '', '', 1, 1, '2023-07-25 06:58:10.579920', 'admin@gmail.com'),
(2, 'pbkdf2_sha256$600000$9wCZMJqRO9kJ6bWJ1glrNX$Vgx1i5chnGcM1G4Ijr+hm/tC+OSIGpHzdsok0VuBBHg=', '2023-08-11 07:59:30.841509', 0, 'Nelson', 'masibo', 'mukule', 0, 1, '2023-08-11 07:59:30.143734', 'nelson@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `users_customuser_groups`
--

CREATE TABLE `users_customuser_groups` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users_customuser_user_permissions`
--

CREATE TABLE `users_customuser_user_permissions` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users_driver`
--

CREATE TABLE `users_driver` (
  `id` bigint(20) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `driving_license_no` varchar(20) NOT NULL,
  `id_passport` varchar(20) NOT NULL,
  `phone_number` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `car_car`
--
ALTER TABLE `car_car`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `number_plate` (`number_plate`),
  ADD KEY `car_car_model_id_c6a3329e` (`model_id`),
  ADD KEY `car_car_make_id_e53f461c_fk_car_carmake_id` (`make_id`),
  ADD KEY `car_car_car_class_id_b7eb688e_fk_car_carclass_id` (`car_class_id`);

--
-- Indexes for table `car_carclass`
--
ALTER TABLE `car_carclass`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `car_carmake`
--
ALTER TABLE `car_carmake`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `car_carmodel`
--
ALTER TABLE `car_carmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `car_carmodel_make_id_e21085bc_fk_car_carmake_id` (`make_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_users_customuser_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `reservations_carinspection`
--
ALTER TABLE `reservations_carinspection`
  ADD PRIMARY KEY (`id`),
  ADD KEY `reservations_carinsp_car_out_id_a438766d_fk_reservati` (`car_out_id`);

--
-- Indexes for table `reservations_carout`
--
ALTER TABLE `reservations_carout`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `id_number` (`id_number`),
  ADD KEY `reservations_carout_payment_method_id_0e8fe027_fk_reservati` (`payment_method_id`);

--
-- Indexes for table `reservations_fuel`
--
ALTER TABLE `reservations_fuel`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reservations_inspectionitem`
--
ALTER TABLE `reservations_inspectionitem`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reservations_inspectionitemstatus`
--
ALTER TABLE `reservations_inspectionitemstatus`
  ADD PRIMARY KEY (`id`),
  ADD KEY `reservations_inspect_car_inspection_id_fbfe8b85_fk_reservati` (`car_inspection_id`),
  ADD KEY `reservations_inspect_inspection_item_id_c31faa69_fk_reservati` (`inspection_item_id`),
  ADD KEY `reservations_inspect_fuel_in_id_97075682_fk_reservati` (`fuel_in_id`),
  ADD KEY `reservations_inspect_fuel_out_id_8bf14f2c_fk_reservati` (`fuel_out_id`);

--
-- Indexes for table `reservations_paymentmethod`
--
ALTER TABLE `reservations_paymentmethod`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `reservations_reservation`
--
ALTER TABLE `reservations_reservation`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `reservation_number` (`reservation_number`),
  ADD KEY `reservations_reservation_car_id_e6fbb4a0_fk_car_car_id` (`car_id`),
  ADD KEY `reservations_reservation_client_id_696a60bf_fk_users_client_id` (`client_id`),
  ADD KEY `reservations_reserva_staff_id_98b1a89b_fk_users_cus` (`staff_id`);

--
-- Indexes for table `reservations_taxes`
--
ALTER TABLE `reservations_taxes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users_client`
--
ALTER TABLE `users_client`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `id_number` (`id_number`);

--
-- Indexes for table `users_customuser`
--
ALTER TABLE `users_customuser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `users_customuser_groups`
--
ALTER TABLE `users_customuser_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_customuser_groups_customuser_id_group_id_76b619e3_uniq` (`customuser_id`,`group_id`),
  ADD KEY `users_customuser_groups_group_id_01390b14_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `users_customuser_user_permissions`
--
ALTER TABLE `users_customuser_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_customuser_user_pe_customuser_id_permission_7a7debf6_uniq` (`customuser_id`,`permission_id`),
  ADD KEY `users_customuser_use_permission_id_baaa2f74_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `users_driver`
--
ALTER TABLE `users_driver`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `driving_license_no` (`driving_license_no`),
  ADD UNIQUE KEY `id_passport` (`id_passport`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;

--
-- AUTO_INCREMENT for table `car_car`
--
ALTER TABLE `car_car`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `car_carclass`
--
ALTER TABLE `car_carclass`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `car_carmake`
--
ALTER TABLE `car_carmake`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `car_carmodel`
--
ALTER TABLE `car_carmodel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=139;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- AUTO_INCREMENT for table `reservations_carinspection`
--
ALTER TABLE `reservations_carinspection`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `reservations_carout`
--
ALTER TABLE `reservations_carout`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `reservations_fuel`
--
ALTER TABLE `reservations_fuel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `reservations_inspectionitem`
--
ALTER TABLE `reservations_inspectionitem`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `reservations_inspectionitemstatus`
--
ALTER TABLE `reservations_inspectionitemstatus`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=70;

--
-- AUTO_INCREMENT for table `reservations_paymentmethod`
--
ALTER TABLE `reservations_paymentmethod`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `reservations_reservation`
--
ALTER TABLE `reservations_reservation`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `reservations_taxes`
--
ALTER TABLE `reservations_taxes`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users_client`
--
ALTER TABLE `users_client`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users_customuser`
--
ALTER TABLE `users_customuser`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `users_customuser_groups`
--
ALTER TABLE `users_customuser_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users_customuser_user_permissions`
--
ALTER TABLE `users_customuser_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users_driver`
--
ALTER TABLE `users_driver`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `car_car`
--
ALTER TABLE `car_car`
  ADD CONSTRAINT `car_car_car_class_id_b7eb688e_fk_car_carclass_id` FOREIGN KEY (`car_class_id`) REFERENCES `car_carclass` (`id`),
  ADD CONSTRAINT `car_car_make_id_e53f461c_fk_car_carmake_id` FOREIGN KEY (`make_id`) REFERENCES `car_carmake` (`id`),
  ADD CONSTRAINT `car_car_model_id_c6a3329e_fk_car_carmodel_id` FOREIGN KEY (`model_id`) REFERENCES `car_carmodel` (`id`);

--
-- Constraints for table `car_carmodel`
--
ALTER TABLE `car_carmodel`
  ADD CONSTRAINT `car_carmodel_make_id_e21085bc_fk_car_carmake_id` FOREIGN KEY (`make_id`) REFERENCES `car_carmake` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_customuser` (`id`);

--
-- Constraints for table `reservations_carinspection`
--
ALTER TABLE `reservations_carinspection`
  ADD CONSTRAINT `reservations_carinsp_car_out_id_a438766d_fk_reservati` FOREIGN KEY (`car_out_id`) REFERENCES `reservations_carout` (`id`);

--
-- Constraints for table `reservations_carout`
--
ALTER TABLE `reservations_carout`
  ADD CONSTRAINT `reservations_carout_payment_method_id_0e8fe027_fk_reservati` FOREIGN KEY (`payment_method_id`) REFERENCES `reservations_paymentmethod` (`id`);

--
-- Constraints for table `reservations_inspectionitemstatus`
--
ALTER TABLE `reservations_inspectionitemstatus`
  ADD CONSTRAINT `reservations_inspect_car_inspection_id_fbfe8b85_fk_reservati` FOREIGN KEY (`car_inspection_id`) REFERENCES `reservations_carinspection` (`id`),
  ADD CONSTRAINT `reservations_inspect_fuel_in_id_97075682_fk_reservati` FOREIGN KEY (`fuel_in_id`) REFERENCES `reservations_fuel` (`id`),
  ADD CONSTRAINT `reservations_inspect_fuel_out_id_8bf14f2c_fk_reservati` FOREIGN KEY (`fuel_out_id`) REFERENCES `reservations_fuel` (`id`),
  ADD CONSTRAINT `reservations_inspect_inspection_item_id_c31faa69_fk_reservati` FOREIGN KEY (`inspection_item_id`) REFERENCES `reservations_inspectionitem` (`id`);

--
-- Constraints for table `reservations_reservation`
--
ALTER TABLE `reservations_reservation`
  ADD CONSTRAINT `reservations_reserva_staff_id_98b1a89b_fk_users_cus` FOREIGN KEY (`staff_id`) REFERENCES `users_customuser` (`id`),
  ADD CONSTRAINT `reservations_reservation_car_id_e6fbb4a0_fk_car_car_id` FOREIGN KEY (`car_id`) REFERENCES `car_car` (`id`),
  ADD CONSTRAINT `reservations_reservation_client_id_696a60bf_fk_users_client_id` FOREIGN KEY (`client_id`) REFERENCES `users_client` (`id`);

--
-- Constraints for table `users_customuser_groups`
--
ALTER TABLE `users_customuser_groups`
  ADD CONSTRAINT `users_customuser_gro_customuser_id_958147bf_fk_users_cus` FOREIGN KEY (`customuser_id`) REFERENCES `users_customuser` (`id`),
  ADD CONSTRAINT `users_customuser_groups_group_id_01390b14_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `users_customuser_user_permissions`
--
ALTER TABLE `users_customuser_user_permissions`
  ADD CONSTRAINT `users_customuser_use_customuser_id_5771478b_fk_users_cus` FOREIGN KEY (`customuser_id`) REFERENCES `users_customuser` (`id`),
  ADD CONSTRAINT `users_customuser_use_permission_id_baaa2f74_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
