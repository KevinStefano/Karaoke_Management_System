-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: databasekms
-- ------------------------------------------------------
-- Server version	5.7.29-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `daftarpemesanan`
--

DROP TABLE IF EXISTS `daftarpemesanan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `daftarpemesanan` (
  `id_pesanan` int(11) NOT NULL,
  `nama` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `nomor_ruangan` int(11) DEFAULT NULL,
  `tanggal` date DEFAULT NULL,
  `waktu_masuk` time DEFAULT NULL,
  `durasi` int(11) DEFAULT NULL,
  `harga_akhir` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_pesanan`),
  KEY `FK_email` (`email`),
  KEY `FKnomorRuangan` (`nomor_ruangan`),
  CONSTRAINT `FK_email` FOREIGN KEY (`email`) REFERENCES `membership` (`email`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FKnomorRuangan` FOREIGN KEY (`nomor_ruangan`) REFERENCES `daftarruangan` (`no_ruangan`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `daftarpemesanan`
--

LOCK TABLES `daftarpemesanan` WRITE;
/*!40000 ALTER TABLE `daftarpemesanan` DISABLE KEYS */;
INSERT INTO `daftarpemesanan` VALUES (1,'Austin','kevin@gmail.com',1,'2019-01-01','10:00:00',60,2000000);
/*!40000 ALTER TABLE `daftarpemesanan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `daftarruangan`
--

DROP TABLE IF EXISTS `daftarruangan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `daftarruangan` (
  `no_ruangan` int(11) NOT NULL AUTO_INCREMENT,
  `tipe` varchar(50) NOT NULL,
  PRIMARY KEY (`no_ruangan`),
  KEY `FK_noRuangan` (`tipe`),
  CONSTRAINT `FK_noRuangan` FOREIGN KEY (`tipe`) REFERENCES `jenisruangan` (`tipe`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `daftarruangan`
--

LOCK TABLES `daftarruangan` WRITE;
/*!40000 ALTER TABLE `daftarruangan` DISABLE KEYS */;
INSERT INTO `daftarruangan` VALUES (3,'Deluxe A-3'),(4,'Deluxe A-4'),(1,'Family A-1'),(2,'Family A-2'),(5,'Reguler B-1'),(6,'Reguler B-2'),(7,'Reguler B-3'),(8,'Reguler B-4');
/*!40000 ALTER TABLE `daftarruangan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dataadmin`
--

DROP TABLE IF EXISTS `dataadmin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dataadmin` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `nama_lengkap` varchar(50) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dataadmin`
--

LOCK TABLES `dataadmin` WRITE;
/*!40000 ALTER TABLE `dataadmin` DISABLE KEYS */;
INSERT INTO `dataadmin` VALUES ('filbert','filbert','Filbert'),('hans','hans','Michael Hans'),('kevin','kevin','Kevin Stefano'),('lio','lio','Lionnarta Savirandy'),('samuel','samuel','Samuel');
/*!40000 ALTER TABLE `dataadmin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jenisruangan`
--

DROP TABLE IF EXISTS `jenisruangan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jenisruangan` (
  `tipe` varchar(50) NOT NULL,
  `kapasitas` int(11) DEFAULT NULL,
  `hargaBiasa` int(11) NOT NULL,
  `hargaDiskon` int(11) DEFAULT NULL,
  PRIMARY KEY (`tipe`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jenisruangan`
--

LOCK TABLES `jenisruangan` WRITE;
/*!40000 ALTER TABLE `jenisruangan` DISABLE KEYS */;
INSERT INTO `jenisruangan` VALUES ('Deluxe A-3',20,1400000,12000000),('Deluxe A-4',10,1000000,800000),('Family A-1',30,2000000,18000000),('Family A-2',25,1700000,15000000),('Reguler B-1',5,700000,670000),('Reguler B-2',4,400000,370000),('Reguler B-3',3,250000,230000),('Reguler B-4',2,75000,70000);
/*!40000 ALTER TABLE `jenisruangan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `membership`
--

DROP TABLE IF EXISTS `membership`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `membership` (
  `email` varchar(50) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `umur` int(11) NOT NULL,
  `alamat` varchar(100) DEFAULT NULL,
  `telepon` varchar(20) DEFAULT NULL,
  `paket_membership` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `membership`
--

LOCK TABLES `membership` WRITE;
/*!40000 ALTER TABLE `membership` DISABLE KEYS */;
INSERT INTO `membership` VALUES ('kevin@gmail.com','Austin',19,'Bekasi','081919191919','Gold');
/*!40000 ALTER TABLE `membership` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pembatalan`
--

DROP TABLE IF EXISTS `pembatalan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pembatalan` (
  `id_pemesanan` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  PRIMARY KEY (`id_pemesanan`,`username`),
  KEY `FK_Pembatalan2` (`username`),
  CONSTRAINT `FK_Pembatalan1` FOREIGN KEY (`id_pemesanan`) REFERENCES `daftarpemesanan` (`id_pesanan`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_Pembatalan2` FOREIGN KEY (`username`) REFERENCES `dataadmin` (`username`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pembatalan`
--

LOCK TABLES `pembatalan` WRITE;
/*!40000 ALTER TABLE `pembatalan` DISABLE KEYS */;
/*!40000 ALTER TABLE `pembatalan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `perubahan`
--

DROP TABLE IF EXISTS `perubahan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `perubahan` (
  `no_ruangan` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  PRIMARY KEY (`no_ruangan`,`username`),
  KEY `FK_Perubahan2` (`username`),
  CONSTRAINT `FK_Perubahan1` FOREIGN KEY (`no_ruangan`) REFERENCES `daftarruangan` (`no_ruangan`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_Perubahan2` FOREIGN KEY (`username`) REFERENCES `dataadmin` (`username`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `perubahan`
--

LOCK TABLES `perubahan` WRITE;
/*!40000 ALTER TABLE `perubahan` DISABLE KEYS */;
INSERT INTO `perubahan` VALUES (5,'hans'),(6,'hans'),(7,'hans'),(1,'kevin'),(2,'kevin'),(3,'kevin'),(4,'kevin'),(8,'lio');
/*!40000 ALTER TABLE `perubahan` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-03 18:45:03
