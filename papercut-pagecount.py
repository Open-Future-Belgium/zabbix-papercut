#!/usr/bin/env python

import urllib
import sys
import json
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("papercut.ini")
serverip = config.get("papercutvars", "papercut-server-ip")
serverauth = config.get("papercutvars", "papercut-authorization-key")


url='http://{0}:9191/api/stats/recent-pages-count?minutes=60&{1}'.format(serverip,serverauth)

response = urllib.urlopen(url)
data = json.loads(response.read())

def main():
  if len(sys.argv)<2:
    print "Run as:\n{0} [recentPagesCount]".format(sys.argv[0])

  elif sys.argv[1]=='recentPagesCount':
    recentPagesCount = data['recentPagesCount']
    print recentPagesCount


if __name__ == '__main__':
    main()

