# getSummaryXMLFiles.py
# fetches each XML file, using the master list of all file URLs

import urllib2
import codecs

filename = 'listOfUrlsForSummariesXML.txt'
lines = open(filename).read().split('\n')

for url in lines:
    # chop off front of long URL
    dateOfXML = url[77:] 
    print "processing",dateOfXML
    try:
        xml = urllib2.urlopen(url).read()
        outfile = codecs.open(dateOfXML,"w")
        outfile.write(xml)
        outfile.close()
    except urllib2.URLError as e:
        print(e.reason)
