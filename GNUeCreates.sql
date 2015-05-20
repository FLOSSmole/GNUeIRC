-- -----------------------------------------------------
-- Table `irc`.`GNUeSummaryItems`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `irc`.`GNUeSummaryItems` (
  `itemid` INT NOT NULL AUTO_INCREMENT,
  `issueid` INT NULL,
  `counter` INT NULL,
  `title` VARCHAR(100) NULL,
  `subject` VARCHAR(100) NULL,
  `archive` VARCHAR(255) NULL,
  `startdate` VARCHAR(45) NULL,
  `enddate` VARCHAR(45) NULL,
  PRIMARY KEY (`itemid`))
ENGINE = MyISAM;


-- -----------------------------------------------------
-- Table `irc`.`GNUeSummaryTopics`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `irc`.`GNUeSummaryTopics` (
  `topicid` INT NOT NULL,
  `itemid` INT NULL,
  `topic` VARCHAR(45) NULL,
  PRIMARY KEY (`topicid`))
ENGINE = MyISAM;


-- -----------------------------------------------------
-- Table `irc`.`GNUeSummaryMentions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `irc`.`GNUeSummaryMentions` (
  `mentionid` INT NOT NULL AUTO_INCREMENT,
  `itemid` INT NULL,
  `topic` VARCHAR(45) NULL,
  PRIMARY KEY (`mentionid`))
ENGINE = MyISAM;


-- -----------------------------------------------------
-- Table `irc`.`GNUeSummaryParaQuotes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `irc`.`GNUeSummaryParaQuotes` (
  `paraquoteid` INT NOT NULL AUTO_INCREMENT,
  `paraid` INT NULL,
  `who` VARCHAR(100) NULL,
  `quote` VARCHAR(200) NULL,
  PRIMARY KEY (`paraquoteid`))
ENGINE = MyISAM;


-- -----------------------------------------------------
-- Table `irc`.`GNUeSummaryPara`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `irc`.`GNUeSummaryPara` (
  `paraid` INT NOT NULL AUTO_INCREMENT,
  `itemid` INT NULL,
  `paracount` INT NULL,
  `para` VARCHAR(500) NULL,
  PRIMARY KEY (`paraid`))
ENGINE = MyISAM;
