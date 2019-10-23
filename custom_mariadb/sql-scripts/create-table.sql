CREATE DATABASE custom_db;

USE custom_db;

CREATE TABLE `some_table` (
  `id` bigint(20) NOT NULL,
  `description` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

