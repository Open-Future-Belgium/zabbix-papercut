#!/usr/bin/env python

import urllib
import sys
import json
import ConfigParser

#config = ConfigParser.ConfigParser()
#config.read("papercut.ini")
#serverip = config.get("vars", "papercut-server-ip")
#serverauth = config.get("vars", "papercut-authorization-key")


#url='http://{0}/api/stats/recent-pages-count?minutes=60&{1}'.format(serverip,serverauth)
url='http://10.5.1.96:9191/api/stats/recent-pages-count?minutes=60&Authorization=nwBe295Hl972zIf35nieMacKBDvkm7Xd'

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
