/*
SQLyog Enterprise - MySQL GUI v6.56
MySQL - 5.5.5-10.1.13-MariaDB : Database - tabe-dac-blockchain
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`tabe-dac-blockchain` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `tabe-dac-blockchain`;

/*Table structure for table `data_files` */

DROP TABLE IF EXISTS `data_files`;

CREATE TABLE `data_files` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `fname` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `block1` longblob,
  `block2` longblob,
  `hash1` varchar(10000) DEFAULT NULL,
  `hash2` varchar(10000) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `time1` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `data_files` */

insert  into `data_files`(`id`,`fname`,`email`,`block1`,`block2`,`hash1`,`hash2`,`date`,`time1`) values (1,'Python','cse.takeoff@gmail.com','Python is an interpreted high-level general-purpose programming language. ... It supports multiple \nprogr','Python is an interpreted high-level general-purpose programming language. ... It supports multiple \nprogramming paradigms, including structured (particularly, procedural), object-oriented and functional\nprogramming. It is often described as a \"batteries included\" language due to its comprehensive standard \nlibrary.','d3bbd24443a18766520a946534b0156d796b2ea3','703ac9912190a7cbde7ea8753a5faa1c1050e859','2021-09-07','17:56:23'),(3,'Java','cse.takeoff@gmail.com','One of the most widely used programming languages, Java is used as the server-side language for most\nback-end development projects, including those i','nvolving big data and Android development. Java is \nalso commonly used for desktop computing, other mobile computing, games, and numerical computing.','ccc0011b8178529a84b328ee3ef85d58cec2a503','d18374b1ade6a335ff48963c1f00e7563d35555f','2021-09-07','18:04:00');

/*Table structure for table `owner` */

DROP TABLE IF EXISTS `owner`;

CREATE TABLE `owner` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `ph` varchar(100) DEFAULT NULL,
  `addr` varchar(100) DEFAULT NULL,
  `sign` varchar(100) DEFAULT 'waiting',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `owner` */

insert  into `owner`(`id`,`name`,`email`,`pwd`,`ph`,`addr`,`sign`) values (1,'lakshmi','cse.takeoff@gmail.com','lakshmi@506','9632587410','Tirupati, AP','m99jYLZooMREN6CiC7DDmw'),(2,'Vasudha','vasudha@gmail.com','vasudha12','9098909890','Tenali, AP','waiting');

/*Table structure for table `request_files` */

DROP TABLE IF EXISTS `request_files`;

CREATE TABLE `request_files` (
  `sno` int(10) NOT NULL AUTO_INCREMENT,
  `id` int(100) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `skey` varchar(100) DEFAULT NULL,
  `status` varchar(200) DEFAULT 'request',
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `request_files` */

insert  into `request_files`(`sno`,`id`,`fname`,`email`,`skey`,`status`) values (1,3,'Java','cse.takeoff@gmail.com',NULL,'request'),(2,3,'Java','cse.takeoff@gmail.com','807954','Accepted'),(3,1,'Python','cse.takeoff@gmail.com','578870','Accepted');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(1900) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `skey` varchar(100) DEFAULT 'pending',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`id`,`name`,`email`,`pwd`,`skey`) values (1,'Keerthana','cse@gmail.com','keerthana123','08b9e68f'),(2,'Fathima','fathima@gmail.com','fathima123','pending');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
