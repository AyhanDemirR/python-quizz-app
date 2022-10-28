DROP TABLE IF EXISTS `questions`;

CREATE TABLE `questions` (
  `QID` int(11) DEFAULT NULL,
  `qstn` text,
  `opA` text,
  `opB` text,
  `opC` text,
  `opD` text,
  `ans` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `reg`;

CREATE TABLE `reg` (
  `name` char(30) DEFAULT NULL,
  `lname` char(30) DEFAULT NULL,
  `email` char(30) DEFAULT NULL,
  `uname` char(30) DEFAULT NULL,
  `p` char(100) DEFAULT NULL,
  `score` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

