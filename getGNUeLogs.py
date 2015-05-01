import urllib2
import codecs

filename = 'listOfUrlsForChatLogs.txt'
lines = open(filename).read().split('\n')

for url in lines:
    dateOfLog = url[-10:]
    print "processing",dateOfLog
    html = urllib2.urlopen(url).read()
    outfile = codecs.open(dateOfLog,"w")
    outfile.write(html)
    outfile.close()
