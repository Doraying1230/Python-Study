/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50716
 Source Host           : localhost
 Source Database       : qiushibaike

 Target Server Type    : MySQL
 Target Server Version : 50716
 File Encoding         : utf-8

 Date: 03/08/2017 16:49:00 PM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `haha`
-- ----------------------------
DROP TABLE IF EXISTS `haha`;
CREATE TABLE `haha` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `content` text NOT NULL,
  `ulike` int(11) NOT NULL,
  `time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `qiushibaike`
-- ----------------------------
DROP TABLE IF EXISTS `qiushibaike`;
CREATE TABLE `qiushibaike` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `content` text NOT NULL,
  `ulike` int(11) NOT NULL,
  `time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `status` int(10) unsigned zerofill NOT NULL DEFAULT '0000000000',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=361 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
