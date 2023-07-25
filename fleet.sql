-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 25, 2023 at 04:43 PM
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
(48, 'Can view reservation', 12, 'view_reservation');

-- --------------------------------------------------------

--
-- Table structure for table `car_car`
--

CREATE TABLE `car_car` (
  `id` bigint(20) NOT NULL,
  `number_plate` varchar(20) NOT NULL,
  `model_id` bigint(20) NOT NULL,
  `year` int(10) UNSIGNED NOT NULL,
  `color` varchar(50) NOT NULL,
  `daily_rate` decimal(8,2) NOT NULL,
  `seating_capacity` int(10) UNSIGNED NOT NULL CHECK (`seating_capacity` >= 0),
  `image` varchar(100) DEFAULT NULL,
  `make_id` bigint(20) DEFAULT NULL,
  `car_class_id` bigint(20) DEFAULT NULL,
  `monthly_rate` decimal(8,2) DEFAULT NULL,
  `weekly_rate` decimal(8,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `car_car`
--

INSERT INTO `car_car` (`id`, `number_plate`, `model_id`, `year`, `color`, `daily_rate`, `seating_capacity`, `image`, `make_id`, `car_class_id`, `monthly_rate`, `weekly_rate`) VALUES
(1, 'ABC123', 1, 2022, 'white', 30.00, 4, 'car_images/1_YD45FLI.png', 1, 8, 20.00, 25.00),
(2, 'GHI789', 2, 2020, 'white', 30.00, 4, 'car_images/2.png', 1, 8, 20.00, 25.00),
(3, 'YZA901', 9, 2022, 'Silver', 45.00, 4, 'car_images/3.png', 13, 4, 35.00, 40.00);

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
(24, '2023-07-25 10:41:53.160196', '1', 'Toyota - RAV4 (2022, white, Seats: 4) - ABC123', 2, '[{\"changed\": {\"fields\": [\"Weekly rate\", \"Monthly rate\"]}}]', 7, 1);

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
(12, 'reservations', 'reservation'),
(5, 'sessions', 'session'),
(11, 'users', 'client'),
(6, 'users', 'customuser');

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
(33, 'reservations', '0002_alter_reservation_discount', '2023-07-25 13:22:14.746894');

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
('dgwwixmj0syxe6l8n7i6wtbz1sqglxvs', '.eJxVizsOwjAQBe_iGkXY3l1sSiTOYT3HazniU2BSIe6eREoB5byZ9zEJ87uluesrTcWcjTWH3y1jvOlzExv2Yec-XB-Y7pfd_l0aelt7BJbIxEXFU60nH4QhhNGWDKZcmaDsIMHGowqQQTlwLCJO2TvzXQCMwDKS:1qOIcU:t3YqGkabJVmz9H_CJgPoU83TK6HI-h49ub6zTElraj4', '2023-08-08 14:02:34.215784'),
('xi5uei6q84cari81ynvlips29akh9pqv', '.eJxVizsOwjAQBe_iGkXY3l1sSiTOYT3HazniU2BSIe6eREoB5byZ9zEJ87uluesrTcWcjTWH3y1jvOlzExv2Yec-XB-Y7pfd_l0aelt7BJbIxEXFU60nH4QhhNGWDKZcmaDsIMHGowqQQTlwLCJO2TvzXQCMwDKS:1qOC03:Shwzr5M1nipzfmYASjP2nV4DHiphu72vnoA3BLyyNvU', '2023-08-08 06:58:27.189679');

-- --------------------------------------------------------

--
-- Table structure for table `reservations_reservation`
--

CREATE TABLE `reservations_reservation` (
  `id` bigint(20) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `rate` decimal(8,2) NOT NULL,
  `discount` decimal(8,2) DEFAULT NULL,
  `car_id` bigint(20) NOT NULL,
  `client_id` bigint(20) NOT NULL,
  `staff_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reservations_reservation`
--

INSERT INTO `reservations_reservation` (`id`, `start_date`, `end_date`, `rate`, `discount`, `car_id`, `client_id`, `staff_id`) VALUES
(1, '2023-07-26', '2023-07-27', 60.00, 0.00, 2, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `users_client`
--

CREATE TABLE `users_client` (
  `id` bigint(20) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `id_number` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users_client`
--

INSERT INTO `users_client` (`id`, `first_name`, `last_name`, `email`, `phone_number`, `id_number`) VALUES
(1, 'NELSON', 'MASIBO', 'nelsonmasibo6@gmail.com', '0704122212', '35100086'),
(2, 'DAVID', 'KIAMA', 'david.kiamaa@gmail.com', '+254722921960', '35100087'),
(3, 'Shynat', 'nganga', 'shynat@gmail.com', '0704122213', '35100088'),
(4, 'kush', 'dinesh', 'kushdinesh98@gmail.com', '0704122214', '35100089');

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
(1, 'pbkdf2_sha256$600000$frBFQjr3Sua0MF4HmyFBAg$We/sB3ciIves35JgonQkAwae0QEDXPb//ddpCOrdRbo=', '2023-07-25 14:02:34.176653', 1, 'admin', '', '', 1, 1, '2023-07-25 06:58:10.579920', 'admin@gmail.com');

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
-- Indexes for table `reservations_reservation`
--
ALTER TABLE `reservations_reservation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `reservations_reservation_car_id_e6fbb4a0_fk_car_car_id` (`car_id`),
  ADD KEY `reservations_reservation_client_id_696a60bf_fk_users_client_id` (`client_id`),
  ADD KEY `reservations_reserva_staff_id_98b1a89b_fk_users_cus` (`staff_id`);

--
-- Indexes for table `users_client`
--
ALTER TABLE `users_client`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `id_number` (`id_number`),
  ADD UNIQUE KEY `users_client_phone_number_53d3743a_uniq` (`phone_number`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `reservations_reservation`
--
ALTER TABLE `reservations_reservation`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `users_client`
--
ALTER TABLE `users_client`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users_customuser`
--
ALTER TABLE `users_customuser`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

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
