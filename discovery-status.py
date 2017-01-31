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
  if len(sys.argv)<2:
    print "Run as:\n{0} [printername]".format(sys.argv[0])

  else:
    printername = sys.argv[1]

    try:
        var = [ i["status"] for i in json_input['printers'] if i["name"] == printername ]
        if var == [u'OK']:
          print 1
        else:
          print 0

    except (ValueError, KeyError, TypeError):
        print "JSON format error"
        print json.dumps(r, indent=2, sort_keys=True, encoding="utf-8")

if __name__ == "__main__":
    main()
