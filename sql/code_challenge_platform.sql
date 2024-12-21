-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 19, 2024 at 04:40 PM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `code_challenge_platform`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
(25, 'Can add challenge', 7, 'add_challenge'),
(26, 'Can change challenge', 7, 'change_challenge'),
(27, 'Can delete challenge', 7, 'delete_challenge'),
(28, 'Can view challenge', 7, 'view_challenge'),
(29, 'Can add test case', 8, 'add_testcase'),
(30, 'Can change test case', 8, 'change_testcase'),
(31, 'Can delete test case', 8, 'delete_testcase'),
(32, 'Can view test case', 8, 'view_testcase');

-- --------------------------------------------------------

--
-- Table structure for table `core_challenge`
--

DROP TABLE IF EXISTS `core_challenge`;
CREATE TABLE IF NOT EXISTS `core_challenge` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `difficulty` varchar(20) NOT NULL,
  `input_format` longtext NOT NULL,
  `output_format` longtext NOT NULL,
  `examples` longtext NOT NULL,
  `template_code` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `core_challenge`
--

INSERT INTO `core_challenge` (`id`, `title`, `description`, `difficulty`, `input_format`, `output_format`, `examples`, `template_code`) VALUES
(13, 'Reverse a String', 'Write a function that takes a string as input and returns the string reversed.', 'Easy', ' A single string s (1 ≤ |s| ≤ 1000), which contains only alphabetic characters.', 'The reversed string.', 'Examples:\r\n\r\nInput: \"hello\"\r\n\r\nOutput: \"olleh\"\r\n\r\nInput: \"world\"\r\n\r\nOutput: \"dlrow\"', 'def reverse_string(s):\r\n    # Write Your Code here\r\n    \r\n\r\n\r\nuser_input = input(\"\")\r\nreversed_string = reverse_string(user_input)\r\nprint(reversed_string)\r\n   \r\n');

-- --------------------------------------------------------

--
-- Table structure for table `core_customuser`
--

DROP TABLE IF EXISTS `core_customuser`;
CREATE TABLE IF NOT EXISTS `core_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `birthday` date DEFAULT NULL,
  `gender` varchar(1) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `profile_picture` varchar(100) DEFAULT NULL,
  `skills` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `core_customuser`
--

INSERT INTO `core_customuser` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `birthday`, `gender`, `location`, `profile_picture`, `skills`) VALUES
(3, 'pbkdf2_sha256$870000$swS5iHi5xd16j9GmPelarI$oHV4wsi+okK4dH82eeTIXPPxjUq8GjUMw7z4pPo8gko=', '2024-11-06 17:59:20.595401', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2024-10-23 10:08:28.226809', NULL, NULL, NULL, NULL, NULL),
(6, 'pbkdf2_sha256$870000$qrQDYBZJmYehDBmh4dByXQ$iqOY01aQTzP/wgcwn77HrWwpjQk/6NxOySV9PrC18GY=', '2024-11-06 17:44:03.156899', 0, 'jayasurya', 'Jayasurya', 'Sudhakaran', 'jayasurya@gmail.com', 0, 1, '2024-11-06 17:08:54.260272', NULL, NULL, NULL, '', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `core_customuser_groups`
--

DROP TABLE IF EXISTS `core_customuser_groups`;
CREATE TABLE IF NOT EXISTS `core_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `core_customuser_groups_customuser_id_group_id_7990e9c6_uniq` (`customuser_id`,`group_id`),
  KEY `core_customuser_groups_customuser_id_976bc4d7` (`customuser_id`),
  KEY `core_customuser_groups_group_id_301aeff4` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `core_customuser_user_permissions`
--

DROP TABLE IF EXISTS `core_customuser_user_permissions`;
CREATE TABLE IF NOT EXISTS `core_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `core_customuser_user_per_customuser_id_permission_49ea742a_uniq` (`customuser_id`,`permission_id`),
  KEY `core_customuser_user_permissions_customuser_id_ebd2ce6c` (`customuser_id`),
  KEY `core_customuser_user_permissions_permission_id_80ceaab9` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `core_testcase`
--

DROP TABLE IF EXISTS `core_testcase`;
CREATE TABLE IF NOT EXISTS `core_testcase` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `input_data` longtext NOT NULL,
  `expected_output` longtext NOT NULL,
  `challenge_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_testcase_challenge_id_44a20f25` (`challenge_id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `core_testcase`
--

INSERT INTO `core_testcase` (`id`, `input_data`, `expected_output`, `challenge_id`) VALUES
(19, 'world', 'dlrow', 13),
(18, 'hello', 'olleh', 13);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(6, 'core', 'customuser'),
(7, 'core', 'challenge'),
(8, 'core', 'testcase');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-10-23 09:45:23.325091'),
(2, 'contenttypes', '0002_remove_content_type_name', '2024-10-23 09:45:23.405471'),
(3, 'auth', '0001_initial', '2024-10-23 09:45:23.633299'),
(4, 'auth', '0002_alter_permission_name_max_length', '2024-10-23 09:45:23.664899'),
(5, 'auth', '0003_alter_user_email_max_length', '2024-10-23 09:45:23.664899'),
(6, 'auth', '0004_alter_user_username_opts', '2024-10-23 09:45:23.664899'),
(7, 'auth', '0005_alter_user_last_login_null', '2024-10-23 09:45:23.684297'),
(8, 'auth', '0006_require_contenttypes_0002', '2024-10-23 09:45:23.684826'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2024-10-23 09:45:23.684826'),
(10, 'auth', '0008_alter_user_username_max_length', '2024-10-23 09:45:23.694996'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2024-10-23 09:45:23.698329'),
(12, 'auth', '0010_alter_group_name_max_length', '2024-10-23 09:45:23.732482'),
(13, 'auth', '0011_update_proxy_permissions', '2024-10-23 09:45:23.732482'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2024-10-23 09:45:23.743995'),
(15, 'core', '0001_initial', '2024-10-23 09:45:24.012669'),
(16, 'admin', '0001_initial', '2024-10-23 09:45:24.199815'),
(17, 'admin', '0002_logentry_remove_auto_add', '2024-10-23 09:45:24.202320'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2024-10-23 09:45:24.202320'),
(19, 'sessions', '0001_initial', '2024-10-23 09:45:24.252129'),
(20, 'core', '0002_customuser_birthday_customuser_gender_and_more', '2024-10-23 14:53:39.137477'),
(21, 'core', '0003_challenge', '2024-10-24 10:15:31.856058'),
(22, 'core', '0004_testcase', '2024-10-27 04:58:28.625929'),
(23, 'core', '0005_challenge_template_code', '2024-10-31 06:50:19.256545');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('j6aw93xp259ujvof5zvnvercfzw6tbcd', 'e30:1t3XwE:LdkBGFm5zjdo0ghSJ5bSDaqhr9KabYu8rwQlFGE7_1E', '2024-11-06 09:45:58.021591'),
('o1g5fh0mixtjjdejszdgzfkvecxa813t', 'e30:1t3YCs:87axrYtylr7y75Ubqb-qPXPxY2S4gPYDNUgPd0erLbk', '2024-11-06 10:03:10.741999'),
('mli3jt4w06rre716fgtnaosdxtsadz2a', 'e30:1t3YJS:tIaemwTOgp7q5Y1gViu_MMXFR52QcDEcoLkM9F-jsgM', '2024-11-06 10:09:58.455841'),
('nbqli0zo6xo6885ju2bqbvoowkzdkuts', 'e30:1t3YgG:ARA9MHppWA37Z8D1AgH3c3aR-jyBKy-3k-uOiA2RWbw', '2024-11-06 10:33:32.573454'),
('rwy7pj80junc3rvs0afhh4n9gn9vclly', '.eJxVjEEOwiAQRe_C2hAcBhCX7j0DYZipVA1NSrsy3l2bdKHb_977L5XyutS0dpnTyOqsrDr8bpTLQ9oG-J7bbdJlass8kt4UvdOurxPL87K7fwc19_qtiUxmfxJ39DaIOBjEYIhggWCgEJiRYkZP0ZYoyMRkTQEEDEXIgXp_APVHOF0:1t4zdd:MzCzVS44m3CYxhVXqdmivAGCEygZjBunvK5AEHW8OKk', '2024-11-10 09:32:45.167738'),
('g5jxh0dnfnpmslu8phyh28rhtkfc4qhl', '.eJxVjDsOwjAQBe_iGll4vf5ASc8ZLHt3hQPIluKkQtwdIqWA9s3Me6mU16WmdcicJlZnherwu5VMD2kb4Htut66pt2Weit4UvdOhr53ledndv4OaR_3WkcCgFHBoJeKJwQJ65GgIskegYA0xOTlS4EAFi-VsI4MJ1mERr94fzl03lQ:1t3d94:mv5BpblvJ0o5-Yw-0fO3LwtPr-b1BRHxMbR6SLXWZbw', '2024-11-06 15:19:34.524947'),
('48oimchiyvuy71asrrc5kliqc6u3ry60', '.eJxVjEEOwiAQRe_C2hAcBhCX7j0DYZipVA1NSrsy3l2bdKHb_977L5XyutS0dpnTyOqsrDr8bpTLQ9oG-J7bbdJlass8kt4UvdOurxPL87K7fwc19_qtiUxmfxJ39DaIOBjEYIhggWCgEJiRYkZP0ZYoyMRkTQEEDEXIgXp_APVHOF0:1t6PYs:2dOzLaWvkOumZk8Vbjzwnz5EUA_Qw-ZloAIADYu0niY', '2024-11-14 07:25:42.099723'),
('fh2owom6aux1u17wsc5h9ac3u86epv91', '.eJxVjEEOwiAQRe_C2hAcBhCX7j0DYZipVA1NSrsy3l2bdKHb_977L5XyutS0dpnTyOqsrDr8bpTLQ9oG-J7bbdJlass8kt4UvdOurxPL87K7fwc19_qtiUxmfxJ39DaIOBjEYIhggWCgEJiRYkZP0ZYoyMRkTQEEDEXIgXp_APVHOF0:1t8kJM:OkQ5cjgEUas17JtANK0Gv446DLm7sVS04g_CIRRMQeI', '2024-11-20 17:59:20.596683');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
