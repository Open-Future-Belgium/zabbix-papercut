#!/usr/bin/env python

import urllib.request as ur
import sys
import json
import codecs

file=open('/etc/zabbix/papercut.conf','r')
for line in file.readlines():
    (key, sep, value) = line.partition('=')
    if key == 'papercut_ip':
        serverip = value[1:-2]
    if key == 'papercut_auth':
        serverauth = value[1:-2]


url='http://{0}/api/health?{1}'.format(serverip,serverauth)
url2='http://{0}/api/stats/held-jobs-count?minutes=10&{1}'.format(serverip,serverauth)
url3='http://{0}/api/stats/recent-pages-count?minutes=60&{1}'.format(serverip,serverauth)

#response = ur.urlopen(url)
reader = codecs.getreader("utf-8")
#json_input = json.load(reader(response))


response = ur.urlopen(url)
data = json.load(reader(response))

response2 = ur.urlopen(url2)
data2 = json.load(reader(response2))

response3 = ur.urlopen(url3)
data3 = json.load(reader(response3))

def main():
  if len(sys.argv)<2:
    print("Run as:\n{0} [version | diskSpaceFreeMB | jvmMemoryUsedPercentage | uptimeHours]".format(sys.argv[0]))

  elif sys.argv[1]=='version':
    version = data['applicationServer']['systemInfo']['version']
    print(version)

  elif sys.argv[1]=='diskSpaceFreeMB':
    diskSpaceFreeMB = data['applicationServer']['systemMetrics']['diskSpaceFreeMB']
    print(diskSpaceFreeMB)

  elif sys.argv[1]=='jvmMemoryUsedPercentage':
    jvmMemoryUsedPercentage = data['applicationServer']['systemMetrics']['jvmMemoryUsedPercentage']
    print(jvmMemoryUsedPercentage)

  elif sys.argv[1]=='uptimeHours':
    uptimeHours = data['applicationServer']['systemMetrics']['uptimeHours']
    print(uptimeHours)

  elif sys.argv[1]=='diskSpaceUsedPercentage':
    diskSpaceUsedPercentage = data['applicationServer']['systemMetrics']['diskSpaceUsedPercentage']
    print(diskSpaceUsedPercentage)

  elif sys.argv[1]=='validlicense':
    validlicense = data['license']['valid']
    print(validlicense)

  elif sys.argv[1]=='licenseRemaining':
    licenseRemaining = data['license']['licenseRemainingDays']
    print(licenseRemaining)

  elif sys.argv[1]=='databaseStatus':
    databaseStatus = data['database']['status']
    print(databaseStatus)

  elif sys.argv[1]=='activeConnections':
    activeConnections = data['database']['activeConnections']
    print(activeConnections)

  elif sys.argv[1]=='maxConnections':
    maxConnections = data['database']['maxConnections']
    print(maxConnections)

  elif sys.argv[1]=='heldJobsCount':
    heldJobsCount = data2['heldJobsCount']
    print(heldJobsCount)

  elif sys.argv[1]=='recentPagesCount':
    recentPagesCount = data3['recentPagesCount']
    print(recentPagesCount)

if __name__ == '__main__':
    main()