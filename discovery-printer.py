#!/usr/bin/env python

import urllib
import sys
import json


serverip="canary.papercut.com"
serverauth='Authorization=0b3ee6f4-5a97-4918-8f1b-3628142093d5'

r = { "data": [] }
domains = []

url='http://{0}/api/health/printers?{1}'.format(serverip,serverauth)

response = urllib.urlopen(url)
json_input = json.loads(response.read())

def main():
    try:
        for i in json_input['printers']:
            r["data"].append( {"{#PRNAME}": i['name']} )

        print json.dumps(r, indent=2, sort_keys=True, encoding="utf-8")

    except (ValueError, KeyError, TypeError):
        print "JSON format error"

if __name__ == "__main__":
    main()
