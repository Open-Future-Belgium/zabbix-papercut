#!/usr/bin/env python

import urllib
import sys
import json

serverip="10.5.1.96:9191"
serverauth='Authorization=nwBe295Hl972zIf35nieMacKBDvkm7Xd'

url='http://{0}/api/health?{1}'.format(serverip,serverauth)
url2='http://{0}/api/stats/held-jobs-count?minutes=10&{1}'.format(serverip,serverauth)
url3='http://{0}/api/stats/recent-pages-count?minutes=60&{1}'.format(serverip,serverauth)

response = urllib.urlopen(url)
data = json.loads(response.read())

response2 = urllib.urlopen(url2)
data2 = json.loads(response2.read())

response3 = urllib.urlopen(url3)
data3 = json.loads(response3.read())

def main():
  if len(sys.argv)<2:
    print "Run as:\n{0} [version | diskSpaceFreeMB | jvmMemoryUsedPercentage | uptimeHours]".format(sys.argv[0])

  elif sys.argv[1]=='version':
    version = data['applicationServer']['systemInfo']['version']
    print version

  elif sys.argv[1]=='diskSpaceFreeMB':
    diskSpaceFreeMB = data['applicationServer']['systemMetrics']['diskSpaceFreeMB']
    print diskSpaceFreeMB

  elif sys.argv[1]=='jvmMemoryUsedPercentage':
    jvmMemoryUsedPercentage = data['applicationServer']['systemMetrics']['jvmMemoryUsedPercentage']
    print jvmMemoryUsedPercentage

  elif sys.argv[1]=='uptimeHours':
    uptimeHours = data['applicationServer']['systemMetrics']['uptimeHours']
    print uptimeHours

  elif sys.argv[1]=='diskSpaceUsedPercentage':
    diskSpaceUsedPercentage = data['applicationServer']['systemMetrics']['diskSpaceUsedPercentage']
    print diskSpaceUsedPercentage

  elif sys.argv[1]=='validlicense':
    validlicense = data['license']['valid']
    print validlicense

  elif sys.argv[1]=='licenseRemaining':
    licenseRemaining = data['license']['licenseRemainingDays']
    print licenseRemaining 

  elif sys.argv[1]=='databaseStatus':
    databaseStatus = data['database']['status']
    print databaseStatus

  elif sys.argv[1]=='activeConnections':
    activeConnections = data['database']['activeConnections']
    print activeConnections

  elif sys.argv[1]=='maxConnections':
    maxConnections = data['database']['maxConnections']
    print maxConnections

  elif sys.argv[1]=='heldJobsCount':
    heldJobsCount = data2['heldJobsCount']
    print heldJobsCount

  elif sys.argv[1]=='recentPagesCount':
    recentPagesCount = data3['recentPagesCount']
    print recentPagesCount

if __name__ == '__main__':
    main()
