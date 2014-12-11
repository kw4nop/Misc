import sys
import feedparser
from colorama import Fore

bugTraqList = "http://seclists.org/rss/bugtraq.rss"
fullDiscList = "http://seclists.org/rss/fulldisclosure.rss"

try:
    if sys.argv[1] == "1":
        feed= feedparser.parse (bugTraqList)
    elif sys.argv[1] == "2":
        feed = feedparser.parse (fullDiscList)
except:
     print ("please type a correct option\n usage: python seclist.py 1"
            "(bugtraq) or 2 (fulldisclosure)")
     sys.exit(0)

print "Welcome to %s list \n more info %s  "%(feed ["channel"] ["title"],
                                              feed ["channel"] ["link"])
for data in range(10):
    print Fore.RED+"#########\n"+Fore.RESET+"[*]%s - %s\n --More info: %s"%(
      feed.entries[data].date,feed.entries[data].title,feed.entries[data].link)
