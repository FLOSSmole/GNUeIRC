# GNUeIRC
Collectors for the GNUe "gold standard" irc summaries and original irc logs

Step 1: make a list of URLs where the logs are. This is stored in listOfUrlsForChatLogs.txt  
This list is made by going to the IRC log archives for the project and collecting all of the log links as shown.

Step 2: collect each log on the list using getGNUeLogs.py  
Despite the URLs being shown as clickable links in Step 1, some of the log URLs are invalid and return no pages: 
*  Logs for dates between 07-Oct-2006 and 23-Jan-2008, inclusive

Step 3: make a list of URLs where the summaries are. This is stored in listOfUrlsForSummariesXML.txt
*  Summaries sometimes skip numbers. 96, 100, 104 are not listed as existing
  
Step 4: Collect each summary
