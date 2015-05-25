-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 25, 2015 at 12:31 PM
-- Server version: 5.5.38-0ubuntu0.14.04.1
-- PHP Version: 5.6.0-1+deb.sury.org~trusty+1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";
-- --------------------------------------------------------

--
-- Table structure for table `GNUeSummaryItems`
--

CREATE TABLE IF NOT EXISTS `GNUeSummaryItems` (
  `itemid` int(11) NOT NULL AUTO_INCREMENT,
  `issueid` int(11) DEFAULT NULL,
  `counter` int(11) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `subject` varchar(100) DEFAULT NULL,
  `archive` varchar(255) DEFAULT NULL,
  `startdate` varchar(45) DEFAULT NULL,
  `enddate` varchar(45) DEFAULT NULL,
  `datasource_id` int(11) NOT NULL,
  PRIMARY KEY (`itemid`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `GNUeSummaryMentions`
--

CREATE TABLE IF NOT EXISTS `GNUeSummaryMentions` (
  `mentionid` int(11) NOT NULL AUTO_INCREMENT,
  `itemid` int(11) DEFAULT NULL,
  `mention` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`mentionid`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `GNUeSummaryPara`
--

CREATE TABLE IF NOT EXISTS `GNUeSummaryPara` (
  `paraid` int(11) NOT NULL AUTO_INCREMENT,
  `itemid` int(11) DEFAULT NULL,
  `paracount` int(11) DEFAULT NULL,
  `para` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`paraid`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `GNUeSummaryParaQuotes`
--

CREATE TABLE IF NOT EXISTS `GNUeSummaryParaQuotes` (
  `paraquoteid` int(11) NOT NULL AUTO_INCREMENT,
  `paraid` int(11) DEFAULT NULL,
  `who` varchar(100) DEFAULT NULL,
  `quote` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`paraquoteid`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `GNUeSummaryTopics`
--

CREATE TABLE IF NOT EXISTS `GNUeSummaryTopics` (
  `topicid` int(11) NOT NULL AUTO_INCREMENT,
  `itemid` int(11) DEFAULT NULL,
  `topic` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`topicid`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8mb4 ;
