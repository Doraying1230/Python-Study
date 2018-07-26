/*
Navicat MySQL Data Transfer

Source Server         : aa
Source Server Version : 50720
Source Host           : localhost:3306
Source Database       : skyeyesdb

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2018-07-25 08:54:34
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `message`
-- ----------------------------
DROP TABLE IF EXISTS `message`;
CREATE TABLE `message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `lawer` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `codeNum` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `telphone` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `address` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of message
-- ----------------------------
INSERT INTO `message` VALUES ('7', '韶关市金叶发展公司', '欧锦梧', '914402001915365284', '8704998\",\"0751-8704998\",\"8177108', '韶关市风采路98号附近公司');
INSERT INTO `message` VALUES ('8', '韶关安能旅游发展有限公司', '应向荣', '91440232770190525Q', '0751-5281770\",\"0751-5286718', '广东省乳源县龙船湾附近公司');
INSERT INTO `message` VALUES ('9', '广东烟草韶关市有限公司', '罗福命', '914402007314418897', '0751-8883116\",\"0751-8883655', '韶关市浈江区南郊三公里金沙小区内京珠北建设管理处综合楼附近公司');
INSERT INTO `message` VALUES ('10', '韶能集团韶关宏大齿轮有限公司', '陈昌镇', '9144020019155323XY', '0751-8172011\",\"0751-8172004', '韶关市武江区沐溪工业园沐溪三路附近公司');
INSERT INTO `message` VALUES ('11', '韶关市公共资产管理中心', ' ', ' ', ' ', ' ');

-- ----------------------------
-- Table structure for `urllist`
-- ----------------------------
DROP TABLE IF EXISTS `urllist`;
CREATE TABLE `urllist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `time` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=222 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of urllist
-- ----------------------------
INSERT INTO `urllist` VALUES ('182', 'https://www.tianyancha.com/company/409253885', '2018-07-25 08:41:56');
INSERT INTO `urllist` VALUES ('183', 'https://www.tianyancha.com/company/776302937', '2018-07-25 08:41:56');
INSERT INTO `urllist` VALUES ('184', 'https://www.tianyancha.com/company/1548012166', '2018-07-25 08:41:56');
INSERT INTO `urllist` VALUES ('185', 'https://www.tianyancha.com/company/265151350', '2018-07-25 08:41:56');
INSERT INTO `urllist` VALUES ('186', 'https://www.tianyancha.com/company/409263178', '2018-07-25 08:41:56');
INSERT INTO `urllist` VALUES ('187', 'https://www.tianyancha.com/company/3177745222', '2018-07-25 08:41:56');
INSERT INTO `urllist` VALUES ('188', 'https://www.tianyancha.com/company/3178690618', '2018-07-25 08:41:56');
INSERT INTO `urllist` VALUES ('189', 'https://www.tianyancha.com/company/2327604848', '2018-07-25 08:41:56');
INSERT INTO `urllist` VALUES ('190', 'https://www.tianyancha.com/company/1606749154', '2018-07-25 08:41:56');
INSERT INTO `urllist` VALUES ('191', 'https://www.tianyancha.com/company/513960737', '2018-07-25 08:41:56');
INSERT INTO `urllist` VALUES ('192', 'https://www.tianyancha.com/company/345406055', '2018-07-25 08:41:56');
INSERT INTO `urllist` VALUES ('193', 'https://www.tianyancha.com/company/817719921', '2018-07-25 08:41:56');
INSERT INTO `urllist` VALUES ('194', 'https://www.tianyancha.com/company/3088118948', '2018-07-25 08:41:56');
INSERT INTO `urllist` VALUES ('195', 'https://www.tianyancha.com/company/3120382676', '2018-07-25 08:41:56');
INSERT INTO `urllist` VALUES ('196', 'https://www.tianyancha.com/company/1625777813', '2018-07-25 08:41:56');
INSERT INTO `urllist` VALUES ('197', 'https://www.tianyancha.com/company/2327300543', '2018-07-25 08:41:56');
INSERT INTO `urllist` VALUES ('198', 'https://www.tianyancha.com/company/1389229336', '2018-07-25 08:41:56');
INSERT INTO `urllist` VALUES ('199', 'https://www.tianyancha.com/company/843679285', '2018-07-25 08:41:56');
INSERT INTO `urllist` VALUES ('200', 'https://www.tianyancha.com/company/2321168029', '2018-07-25 08:41:56');
INSERT INTO `urllist` VALUES ('201', 'https://www.tianyancha.com/company/691283333', '2018-07-25 08:41:56');
INSERT INTO `urllist` VALUES ('202', 'https://www.tianyancha.com/company/2746583812', '2018-07-25 08:41:59');
INSERT INTO `urllist` VALUES ('203', 'https://www.tianyancha.com/company/1332342788', '2018-07-25 08:41:59');
INSERT INTO `urllist` VALUES ('204', 'https://www.tianyancha.com/company/2353842247', '2018-07-25 08:41:59');
INSERT INTO `urllist` VALUES ('205', 'https://www.tianyancha.com/company/831114302', '2018-07-25 08:41:59');
INSERT INTO `urllist` VALUES ('206', 'https://www.tianyancha.com/company/527275639', '2018-07-25 08:41:59');
INSERT INTO `urllist` VALUES ('207', 'https://www.tianyancha.com/company/831053232', '2018-07-25 08:41:59');
INSERT INTO `urllist` VALUES ('208', 'https://www.tianyancha.com/company/2323641481', '2018-07-25 08:41:59');
INSERT INTO `urllist` VALUES ('209', 'https://www.tianyancha.com/company/3101032181', '2018-07-25 08:41:59');
INSERT INTO `urllist` VALUES ('210', 'https://www.tianyancha.com/company/3123635520', '2018-07-25 08:41:59');
INSERT INTO `urllist` VALUES ('211', 'https://www.tianyancha.com/company/364045773', '2018-07-25 08:41:59');
INSERT INTO `urllist` VALUES ('212', 'https://www.tianyancha.com/company/1372211471', '2018-07-25 08:41:59');
INSERT INTO `urllist` VALUES ('213', 'https://www.tianyancha.com/company/2784505337', '2018-07-25 08:41:59');
INSERT INTO `urllist` VALUES ('214', 'https://www.tianyancha.com/company/1443606320', '2018-07-25 08:41:59');
INSERT INTO `urllist` VALUES ('215', 'https://www.tianyancha.com/company/3074952670', '2018-07-25 08:42:00');
INSERT INTO `urllist` VALUES ('216', 'https://www.tianyancha.com/company/830512877', '2018-07-25 08:42:00');
INSERT INTO `urllist` VALUES ('217', 'https://www.tianyancha.com/company/638418516', '2018-07-25 08:42:00');
INSERT INTO `urllist` VALUES ('218', 'https://www.tianyancha.com/company/1356424462', '2018-07-25 08:42:00');
INSERT INTO `urllist` VALUES ('219', 'https://www.tianyancha.com/company/1414801628', '2018-07-25 08:42:00');
INSERT INTO `urllist` VALUES ('220', 'https://www.tianyancha.com/company/1422372088', '2018-07-25 08:42:00');
INSERT INTO `urllist` VALUES ('221', 'https://www.tianyancha.com/company/422414798', '2018-07-25 08:42:00');
