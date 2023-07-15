-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	5.7.34-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `book_details`
--

DROP TABLE IF EXISTS `book_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_details` (
  `acc_no` int(11) NOT NULL,
  `book_name` varchar(120) DEFAULT NULL,
  `author_name` varchar(40) NOT NULL,
  `genre` varchar(40) DEFAULT NULL,
  `availability` varchar(40) DEFAULT NULL,
  `language` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`acc_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_details`
--

LOCK TABLES `book_details` WRITE;
/*!40000 ALTER TABLE `book_details` DISABLE KEYS */;
INSERT INTO `book_details` VALUES (1000,'Harry Potter and the Philosophers Stone','J.K. Rowling','Fantasy','Unavailable','English'),(1001,'Harry Potter and the Chamber of Secrets','J.K. Rowling','Fantasy','Available','English'),(1002,'Harry Potter and the Prisoner of Azkaban','J.K. Rowling','Fantasy','Available','English'),(1003,'Harry Potter and the Goblet of Fire','J.K. Rowling','Fantasy','Available','English'),(1004,'Harry Potter and the Order of the Phoenix','J.K. Rowling','Fantasy','Available','English'),(1005,'Harry Potter and the Half-Blood Prince','J.K. Rowling','Fantasy','Available','English'),(1006,'Harry Potter and the Deathly Hallows','J.K. Rowling','Fantasy','Available','English'),(1007,'The Tales of Beedle the Bard','J.K. Rowling','Fantasy','Available','English'),(1008,'Quidditch Through the Ages','J.K. Rowling','Fantasy','Available','English'),(1009,'The Ickabog','J.K. Rowling','Fantasy','Unavailable','English'),(2000,'Chronicles of Narnia : The Magicians Nephew','C.S. Lewis','Fantasy','Available','English'),(2001,'Chronicles of Narnia : The Lion, The Witch & The Wardrobe','C.S. Lewis','Fantasy','Available','English'),(2002,'Chronicles of Narnia : The Horse and His Boy','C.S. Lewis','Fantasy','Available','English'),(2003,'Chronicles of Narnia : Prince Caspian','C.S. Lewis','Fantasy','Available','English'),(2004,'Chronicles of Narnia : The Voyage of the Dawn Treader','C.S. Lewis','Fantasy','Available','English'),(2005,'Chronicles of Narnia : The Silver Chair','C.S. Lewis','Fantasy','Available','English'),(2006,'Chronicles of Narnia : The Last Battle','C.S. Lewis','Fantasy','Available','English'),(2007,'The Secret','Rhonda Byrne','Self-Help','Available','English'),(2008,'Somnath','Acharya Chatursen','Historical Fiction','Available','Hindi'),(2009,'The Immortals of Meluha','Amish Tripathi','Historical Fiction','Available','English'),(3000,'The Secret of the Nagas','Amish Tripathi','Historical Fiction','Available','English'),(3001,'The Oath of the Vayuputras','Amish Tripathi','Historical Fiction','Available','English'),(3002,'Turbulence: A True Story of Survival','Annette Herfkens','Autobiography','Available','English'),(3003,'The Power of Habit','Charles Duhigg','Self-Help','Available','English'),(3004,'Type Talk','Otto Kroeger & Janet M. Thuesen','Psychology','Available','English'),(3005,'Linda Goodmans Sun signs','Linda Goodman','Astrology','Available','English'),(3006,'Murder on the Orient Express','Agatha Christie','Detective fiction','Available','English'),(3007,'The A.B.C. Murders','Agatha Christie','Detective fiction','Available','English'),(3008,'And Then There Were None','Agatha Christie','Detective fiction','Available','English'),(3009,'The Diary of a Young Girl','Anne Frank','Autobiography','Available','English'),(4000,'Indian Folk Tales','Ruskin Bond','Children','Available','English'),(4001,'The Canterville Ghost','Oscar Wilde','Humour','Available','English'),(4002,'Charlie and the Chocolate Factory','Roald Dahl','Children','Available','English'),(4003,'The Picture Of Dorian Gray','Oscar Wilde','Philosophy','Available','English'),(4004,'Stories by Munshi Prem Chand','Munshi Prem Chand','Hindi Literature','Available','Hindi'),(4005,'Stories by Ravindranath Tagore','Ravindranath Tagore','Hindi Literature','Available','Hindi'),(4006,'Stories by Manu Bhandari','Manu Bhandari','Hindi Literature','Available','Hindi'),(4007,'Stories by Mahadevi Verma','Mahadevi Verma','Hindi Literature','Available','Hindi'),(4008,'Twilight','Stephanie Meyer','Young Adult Fantasy','Available','English'),(4009,'New Moon','Stephanie Meyer','Young Adult Fantasy','Available','English'),(5000,'Eclipse','Stephanie Meyer','Young Adult Fantasy','Available','English'),(5001,'Breaking Dawn','Stephanie Meyer','Young Adult Fantasy','Available','English');
/*!40000 ALTER TABLE `book_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `issued`
--

DROP TABLE IF EXISTS `issued`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `issued` (
  `m_id` int(11) NOT NULL,
  `book_acc_no` int(11) NOT NULL,
  `book_name` varchar(120) DEFAULT NULL,
  `author` varchar(100) DEFAULT NULL,
  `f_name` varchar(100) DEFAULT NULL,
  `phone_no` int(11) DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  `Date_issued` date DEFAULT NULL,
  `Date_returned` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `issued`
--

LOCK TABLES `issued` WRITE;
/*!40000 ALTER TABLE `issued` DISABLE KEYS */;
INSERT INTO `issued` VALUES (11,4000,'Indian Folk Tales','Ruskin Bond','Mark',1234567,'RETURNED','2022-01-27','2022-01-27'),(11,1000,'Harry Potter and the Philosophers Stone','J.K. Rowling','Mark',1234567,'ISSUED','2022-01-27',NULL);
/*!40000 ALTER TABLE `issued` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member_details`
--

DROP TABLE IF EXISTS `member_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member_details` (
  `member_id` int(11) NOT NULL,
  `first_name` varchar(40) NOT NULL,
  `last_name` varchar(40) NOT NULL,
  `address_` varchar(40) NOT NULL,
  `dob` date DEFAULT NULL,
  `phone_no` varchar(20) DEFAULT NULL,
  `pass_key` varchar(40) DEFAULT NULL,
  `email_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member_details`
--

LOCK TABLES `member_details` WRITE;
/*!40000 ALTER TABLE `member_details` DISABLE KEYS */;
INSERT INTO `member_details` VALUES (11,'Mark','Lee','1,Inception Street,Neo City','1999-04-02','1234567','onyourmark','mork@prettygrass.com'),(22,'Mafalda','Hopkirk','2,The Seed, Neo City','1945-07-20','2345678','muffinhop','icecrystal@mom.com'),(33,'Johnny','Suh','3,Sputnick Road, Neo City','1990-09-09','3456789','jcc','notmyproblem@jfe.com'),(44,'Katsuki','Bakugo','4,Godric Hollow, Ncity','2000-05-01','4567890','lordexplosionmurder','starrypuma@mha.com'),(55,'Rowena','Ravenclaw','5,Snorkacks Hill, Laputa','1999-08-18','1023456','phoenix','dareyouto@trickme.com'),(66,'Yangyang','Liu','6,Elysian Place, Laputa','2000-11-03','2034567','bella','myson11@lowlow.com'),(77,'Luna','Lovegood','7,Mystic Falls, Ncity','2004-12-25','3045678','heliopaths','turbulent@paradise.com'),(88,'Shoto','Todoroki','8,The Waterfall, Vercity','2000-06-22','4056789','coldsoba','fireice@robertfrost.com'),(99,'Izuku','Midoriya','9,U.A. School','2000-02-22','7890123','allmightjr','green@strawberry.com'),(100,'Gojo','Satauro','17,Ikigai Lake,Laputa','1999-09-19','2819091820','baka','sensei@thecoolest.com'),(111,'Itadori','Yuji','9,Jujutsu High,Tokyo','2004-08-25','3981930930','enfp','flabbergasted@me.com'),(127,'Lune','Fleur','Turnip Turn, Lake Yamanoko','2003-06-24','1271271270','Czennie','felicity@feliznavidad.com');
/*!40000 ALTER TABLE `member_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-01 13:46:05
