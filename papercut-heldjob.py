#!/usr/bin/env python

import urllib
import sys
import json
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("papercut.ini")
serverip = config.get("vars", "papercut-server-ip")
serverauth = config.get("vars", "papercut-authorization-key")

url='http://{0}/api/stats/held-jobs-count?minutes=10&{1}'.format(serverip,serverauth)

response = urllib.urlopen(url)
data = json.loads(response.read())

def main():
  if len(sys.argv)<2:
    print "Run as:\n{0} [heldJobsCount]".format(sys.argv[0])

  elif sys.argv[1]=='heldJobsCount':
    heldJobsCount = data['heldJobsCount']
    print heldJobsCount


if __name__ == '__main__':
    main()
