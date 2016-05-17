#-*- coding: utf-8 -*-
# RASSec
import json
import sys
import os
import requests
reload(sys)
sys.setdefaultencoding('utf-8')
from datetime import datetime
os.system('echo start time %s > log.txt' % datetime.now())
fname = 'domain(118212410).txt'
tmpfile = 'tmp.json'
fw = open(tmpfile,'w')
fd = open(fname)
mid = 1
count = 0
head = {}
index = 'bigdata'
fw = open(tmpfile,'w')
for line in fd:
    if line:
        if line:
            count = count + 1
            server = line.split(',')[0]
            ip = line.split(',')[1].replace('\n','')
            mpdata={
			 	"ip":ip,
			 	"server":server
			}
            print mpdata
            requests.post("http://localhost:9200/bigdata/data",data=json.dumps(mpdata))
os.system('echo end time %s >> log.txt' % datetime.now())            
fd.close()
fw.close()