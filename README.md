# GNUeIRC
Collectors for the GNUe "gold standard" irc summaries and original irc logs

##Original Logs

Step 1: Make a list of URLs where the logs are. 
*  This is stored in listOfUrlsForChatLogs.txt  
*  This list is made by going to the IRC log archives for the project and collecting all of the log links as shown.

Step 2: Collect each log on the list using getGNUeLogs.py 
*  Some of the files listed are actually missing 
*  This is due to one of two factors: either the IRC server was not running those days (unlikely) or the files were just not indexed by archive.org:
*  2006-10-06 through 2006-11-28
*  2006-11-30 through 2006-12-17
*  2006-12-19 through 2008-01-23
*  2008-01-29 through 2008-02-04

Step 3: Create database tables using GNUeLogCreates.sql 
*  There is one table to hold the parsed logfiles 

Step 4: Parse logfiles 
*  This populates the one GNUe log database table
*  Note that the original log files have no timestamps
*  The dates are constructed via the file name

##Summaries of Logs

Step 1: Make a list of URLs where the summaries are. This is stored in listOfUrlsForSummariesXML.txt
*  Summaries sometimes skip numbers: summaries 96, 100, and 104 do not exist
  
Step 2: Collect each summary using getSummaryXML.py  
*  This creates a list of 122 XML summary files on disk

Step 3: Create the database tables using GNUeCreates.sql
*  There are five tables with logical relationships (no FK enforcement)

Step 4: Parse the summaries using parseSummaryXML.py
*  This populates the five GNUe database tables. 
*  We populate one line in the FLOSSmole datasources table manually: 
```
INSERT INTO `ossmole_merged`.`forges` (`forge_id`, `forge_abbr`, `forge_long_name`, `forge_home_page`, `is_forge`, `is_directory`, `is_other`, `established`, `organization`) VALUES ('67', 'GNUe', 'GNUe Traffic IRC summaries', 'https://web.archive.org/web/20080509160725/http://www.gnuenterprise.org/irc-logs/', '0', '0', '1', '2001', 'GNUenterprise');
```
