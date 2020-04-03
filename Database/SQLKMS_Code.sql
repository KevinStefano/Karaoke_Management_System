DROP DATABASE IF EXISTS `databaseKMS`;
CREATE DATABASE `databaseKMS`; 
USE `databaseKMS`;


CREATE TABLE `JenisRuangan` (
	`tipe` varchar(50) NOT NULL,
	`kapasitas` int,
	`hargaBiasa` int NOT NULL,
    `hargaDiskon` int,
	PRIMARY KEY(`tipe`)
);

INSERT INTO `JenisRuangan` (`tipe`,`kapasitas`,`hargaBiasa`,`hargaDiskon`)
VALUES
	('Family A-1',30,2000000,18000000),
    ('Family A-2',25,1700000,15000000),
    ('Deluxe A-3',20,1400000,12000000),
    ('Deluxe A-4',10,1000000,800000),
    ('Reguler B-1',5,700000,670000),
    ('Reguler B-2',4,400000,370000),
    ('Reguler B-3',3,250000,230000),
    ('Reguler B-4',2,75000,70000);
    
    
CREATE TABLE `DaftarRuangan` (
  `no_ruangan` int NOT NULL AUTO_INCREMENT,
  `tipe` varchar(50) NOT NULL,
	PRIMARY KEY(`no_ruangan`),
	CONSTRAINT `FK_noRuangan` 
		FOREIGN KEY (`tipe`) 
		REFERENCES `JenisRuangan`(`tipe`) 
        ON UPDATE CASCADE 
        ON DELETE CASCADE
);

INSERT INTO `DaftarRuangan` (`no_ruangan`, `tipe`)
VALUES
	(001, 'Family A-1'),
    (002, 'Family A-2'),
    (003, 'Deluxe A-3'),
    (004, 'Deluxe A-4'),
    (005, 'Reguler B-1'),
    (006, 'Reguler B-2'),
    (007, 'Reguler B-3'),
    (008, 'Reguler B-4');
    
CREATE TABLE `DataAdmin` (
	`username` VARCHAR(50) NOT NULL,
    `password` VARCHAR(50) NOT NULL,
    `nama_lengkap` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`username`)
);

INSERT INTO `DataAdmin` (`username`,`password`,`nama_lengkap`)
VALUES
	('kevin', 'kevin', 'Kevin Stefano'),
    ('hans', 'hans', 'Michael Hans'),
    ('samuel', 'samuel', 'Samuel'),
    ('lio','lio','Lionnarta Savirandy'),
    ('filbert','filbert','Filbert');
    
CREATE TABLE `Perubahan` (
	`no_ruangan` int NOT NULL,
    `username` VARCHAR(50) NOT NULL,
    CONSTRAINT `PK_Perubahan` PRIMARY KEY (`no_ruangan`, `username`),
    CONSTRAINT `FK_Perubahan1`
		FOREIGN KEY (`no_ruangan`) 
		REFERENCES `DaftarRuangan` (`no_ruangan`) 
        ON UPDATE CASCADE 
        ON DELETE CASCADE,
	CONSTRAINT `FK_Perubahan2`
		FOREIGN KEY (`username`) 
		REFERENCES `DataAdmin` (`username`) 
        ON UPDATE CASCADE 
        ON DELETE CASCADE
);

INSERT INTO `Perubahan` (`username`,`no_ruangan`)
VALUES 
	('kevin', 001),
    ('kevin', 002),
    ('kevin', 003),
    ('kevin', 004),
    ('hans', 005),
    ('hans', 006),
    ('hans', 007),
    ('lio', 008);
 
CREATE TABLE `Membership` (
	`email` VARCHAR(50) NOT NULL PRIMARY KEY,
    `nama`	VARCHAR(50) NOT NULL,
    `umur` INT NOT NULL,
    `alamat` VARCHAR(100),
    `telepon` VARCHAR(20),
    `paket_membership` VARCHAR(50)
);

INSERT INTO `Membership` 
VALUES
	('kevin@gmail.com','Austin',19,'Bekasi','081919191919', 'Gold');


CREATE TABLE `DaftarPemesanan` (
	`id_pesanan` int NOT NULL PRIMARY KEY,
    `nama` VARCHAR (50),
    `email` VARCHAR(50),
    `nomor_ruangan` int,
    `tanggal` DATE,
    `waktu_masuk` TIME,
    `durasi` int,
    `harga_akhir` int,
     CONSTRAINT `FK_email`
		FOREIGN KEY (`email`) 
		REFERENCES `Membership` (`email`) 
        ON UPDATE CASCADE 
        ON DELETE CASCADE,
	CONSTRAINT `FKnomorRuangan`
		FOREIGN KEY (`nomor_ruangan`) 
		REFERENCES `DaftarRuangan` (`no_ruangan`) 
        ON UPDATE CASCADE 
        ON DELETE CASCADE
);

INSERT INTO `DaftarPemesanan`
VALUES
	(001,'Austin','kevin@gmail.com',001,'2019-01-01','10:00:00',60,2000000);



CREATE TABLE `Pembatalan` (
	`id_pemesanan` int NOT NULL,
    `username` VARCHAR(50) NOT NULL,
    CONSTRAINT `PK_Pembatalan` PRIMARY KEY (`id_pemesanan`, `username`),
    CONSTRAINT `FK_Pembatalan1`
		FOREIGN KEY (`id_pemesanan`) 
		REFERENCES `DaftarPemesanan` (`id_pesanan`) 
        ON UPDATE CASCADE 
        ON DELETE CASCADE,
	CONSTRAINT `FK_Pembatalan2`
		FOREIGN KEY (`username`) 
		REFERENCES `DataAdmin` (`username`) 
        ON UPDATE CASCADE 
        ON DELETE CASCADE
);

    

    
    
