from bs4 import BeautifulSoup
import io
import MySQLdb
from os import listdir
from os.path import isfile, join

datasource_id = 48038
path = 'XMLsummaries'

# Open database connection
db = MySQLdb.connect(host="grid6.cs.elon.edu", 
    user="user", 
    passwd="password", 
    db="irc", 
    use_unicode=True, 
    charset="utf8")
cursor = db.cursor()
cursor.execute('SET NAMES utf8mb4')
cursor.execute('SET CHARACTER SET utf8mb4')
cursor.execute('SET character_set_connection=utf8mb4')

files = [ f for f in listdir(path) if isfile(join(path,f)) ]
for filename in files:
    print 'reading ', filename
    #xml = open(join(path,filename)).read()
    xml  = io.open(join(path,filename), 'r', encoding='utf8')

    soup = BeautifulSoup(xml)
    issueid = soup.issue.get('num')
    counter = 0
    autoincval = 0
    
    for sec in soup.find_all('section'):
        counter += 1
        title     = sec.get('title')
        subject   = sec.get('subject')
        archive   = sec.get('archive')
        startdate = sec.get('startdate')
        enddate   = sec.get('enddate')
        
        '''
        print '==='
        print 'datasource', datasource_id
        print 'issueid', issueid
        print 'counter:',   counter
        print 'title:',    title
        print 'subject:',  subject
        print 'archive:',  archive
        print 'startdate:',startdate
        print 'enddate:',  enddate
        '''
        
        try:
            cursor.execute(u"INSERT INTO GNUeSummaryItems(itemid, issueid, counter, title, subject, archive, startdate, enddate, datasource_id) \
                            VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)",
                            (issueid, counter, title, subject, archive, startdate, enddate, datasource_id))
            db.commit() 
            autoincval = cursor.lastrowid
            
        except MySQLdb.Error as error:
            print(error)
            db.rollback()    

        for topic in sec.find_all('topic'):
            top = topic.string

            try:
                cursor.execute(u"INSERT INTO GNUeSummaryTopics(topicid, itemid, topic) \
                                VALUES (NULL, %s, %s)",(autoincval, top))
                db.commit() 
                
            except MySQLdb.Error as error:
                print(error)
                db.rollback()    
            
        for mention in sec.find_all('mention'):
            ment = mention.string
            mentu = ment.encode('utf-8').strip()
  
            try:
                cursor.execute(u"INSERT INTO GNUeSummaryMentions(mentionid, itemid, mention) \
                                VALUES (NULL, %s, %s)",(autoincval, mentu))
                db.commit() 
                
            except MySQLdb.Error as error:
                print(error)
                db.rollback()    
            
        paracount = 0
        paraautoincval = 0
        for p in sec.find_all('p'):
            paracount += 1
            para = p.get_text().replace('\r\n',' ')

            try:
                cursor.execute(u"INSERT INTO GNUeSummaryPara(paraid, itemid, paracount, para) \
                                VALUES (NULL, %s, %s, %s)",(autoincval, paracount, para))
                db.commit()
                # get last used paragraph id (autoincrement)
                paraautoincval = cursor.lastrowid
                 
    
            except MySQLdb.Error as error:
                print(error)
                db.rollback()    
            
            for quote in p.find_all('quote'):   
                who = quote.get('who') 
                quo = quote.get_text().replace('\r\n',' ')     
                  
                try:
                    cursor.execute(u"INSERT INTO GNUeSummaryParaQuotes(paraquoteid, paraid, who, quote) \
                                    VALUES (NULL, %s, %s, %s)",(paraautoincval, who, quo))
                    db.commit() 
                        
                except MySQLdb.Error as error:
                    print(error)
                    db.rollback()    
# disconnect from server
db.close()
