/*
SQLyog Enterprise - MySQL GUI v6.56
MySQL - 5.5.5-10.4.21-MariaDB : Database - tabe-dac-blockchain
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`tabe-dac-blockchain` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `tabe-dac-blockchain`;

/*Table structure for table `attacker` */

DROP TABLE IF EXISTS `attacker`;

CREATE TABLE `attacker` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `filename` varchar(100) DEFAULT NULL,
  `owneremail` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `attacker` */

insert  into `attacker`(`id`,`filename`,`owneremail`,`status`) values (1,'amazon','datapwner@gmail.com','attacked'),(2,'amazon','datapwner@gmail.com','attacked'),(3,'amazon','datapwner@gmail.com','attacked');

/*Table structure for table `data_files` */

DROP TABLE IF EXISTS `data_files`;

CREATE TABLE `data_files` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `fname` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `block1` longblob DEFAULT NULL,
  `block2` longblob DEFAULT NULL,
  `hash1` varchar(10000) DEFAULT NULL,
  `hash2` varchar(10000) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `time1` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `data_files` */

insert  into `data_files`(`id`,`fname`,`email`,`block1`,`block2`,`hash1`,`hash2`,`date`,`time1`) values (1,'amazon','datapwner@gmail.com','28-05-22\n\nTK14570 - 3:00 exec - completed\nTK15589 - 10:30 Expl - Completed\nTK14211 - Errors : 10\nTK22865 - Execution : 5\nTK20238 - call - completed -student need the project in AWS\nTK14896 - offline - completed\n\n\n30-05-22\n\nTK12126- expl - 5:00\nTK15334- error - 4:30\nTK14211-error -1:00 -  Errors',' Completed\nTK13864- demo - 000\nTK44420- execu - 3:00\n\n31-05-22\n\nTK15125 - exe -  10:00 \nTK13139 - exe - 3:00 \nTK15305 - doubts - 12:30\nTk41312 - total exp -4:30\nTK44238 - exe -   11:00\nTK18162 - doubts -5:30 - Fathima\n\n\n\nhttps://us05web.zoom.us/j/82783335679?pwd=R25GNnNWRmZCMHpxZVI2RGpGMWdZdz09\n','84676065499906212700249386714784986602381535422885','84676065499906212700249386714784986602381535422885','2022-09-17','16:59:52');

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `owner` */

insert  into `owner`(`id`,`name`,`email`,`pwd`,`ph`,`addr`,`sign`) values (1,'dataowner','datapwner@gmail.com','Malli@12345678','9848035289','hello','AuPc0rnMQhAK0vRWblandg');

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `request_files` */

insert  into `request_files`(`sno`,`id`,`fname`,`email`,`skey`,`status`) values (1,1,'amazon','user@gmail.com','655611','Accepted'),(2,1,'amazon','user@gmail.com','655611','Accepted');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(1900) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `skey` varchar(100) DEFAULT 'pending',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`id`,`name`,`email`,`pwd`,`skey`) values (1,'user','user@gmail.com','User@12345678','48b3f9c5');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
