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


r = { "data": [] }
domains = []

url='http://{0}/api/health/printers?{1}'.format(serverip,serverauth)
response = ur.urlopen(url)
reader = codecs.getreader("utf-8")
json_input = json.load(reader(response))

def main():
    try:
        for i in json_input['printers']:
            r["data"].append( {"{#PRNAME}": i['name']} )

        print(json.dumps(r, indent=2, sort_keys=True))

    except (ValueError, KeyError, TypeError):
        print("JSON format error")

if __name__ == "__main__":
    main()
