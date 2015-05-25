# GNUeIRC
Collectors for the GNUe "gold standard" irc summaries and original irc logs

Step 1: Make a list of URLs where the logs are. 
*  This is stored in listOfUrlsForChatLogs.txt  
*  This list is made by going to the IRC log archives for the project and collecting all of the log links as shown.

Step 2: Collect each log on the list using getGNUeLogs.py  
*  Despite the URLs being shown as clickable links in Step 1, some of the log URLs are invalid and return no pages. 
*  For example, logs for dates between 07-Oct-2006 and 23-Jan-2008, inclusive are not available

Step 3: Make a list of URLs where the summaries are. This is stored in listOfUrlsForSummariesXML.txt
*  Summaries sometimes skip numbers: summaries 96, 100, and 104 do not exist
  
Step 4: Collect each summary using getSummaryXML.py  
*  This creates a list of 122 XML summary files on disk

Step 5: Create the SQL tables using GNUeCreates.sql
*  There are five tables with logical relationships (no FK enforcement)

Step 6: Parse the summaries using parseSummaryXML.py
*  This populates the five GNUe database tables. 
*  We populate one line in the FLOSSmole datasources table manually: 
```
INSERT INTO `ossmole_merged`.`forges` (`forge_id`, `forge_abbr`, `forge_long_name`, `forge_home_page`, `is_forge`, `is_directory`, `is_other`, `established`, `organization`) VALUES ('67', 'GNUe', 'GNUe Traffic IRC summaries', 'https://web.archive.org/web/20080509160725/http://www.gnuenterprise.org/irc-logs/', '0', '0', '1', '2001', 'GNUenterprise');
```
