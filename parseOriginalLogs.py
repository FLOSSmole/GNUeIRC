import re
import codecs
import MySQLdb
from os import listdir
from os.path import isfile, join

datasource_id = 48038

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

path = 'chatLogs'
files = [ f for f in listdir(path) if not f.startswith('.') and isfile(join(path,f)) ]
for filename in files:
    print 'reading ', filename
    
    # these IRC files have some windows encoding in them
    log = codecs.open(join(path,filename), 'r', encoding='utf-8', errors='ignore')
    
    linecount   = 0
    username    = ''
    linemessage = ''
    linetype    = ''
    for line in log:
        linecount += 1
        # case 1: user message
        patternMessage = re.compile(ur'^<(.+?)>\s(.+?)$', re.UNICODE)
    
        if patternMessage.search(line):
            username = patternMessage.search(line).group(1)   
            linemessage = patternMessage.search(line).group(2)
            linetype = 'message' 
        
        # case 2: system message
        else:
            linetype = 'system'
            linemessage = line
        
        print 'linecount:',linecount,': ', linetype
        
        try:
            cursor.execute(u"INSERT INTO GNUeIRCLogs(date_of_log, line_num, type, send_user, line_message, datasource_id) \
                            VALUES (%s, %s, %s, %s, %s, %s)",
                            (filename, linecount, linetype, username, linemessage, datasource_id))
            db.commit() 
            username = ''
            line_message = ''
        except MySQLdb.Error as error:
            print(error)
            db.rollback()
        
    log.close()
# disconnect from server
db.close()
