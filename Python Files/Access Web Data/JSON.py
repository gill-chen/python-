import json
import urllib

serviceurl = "http://python-data.dr-chuck.net/comments_298763.json"

uh = urllib.urlopen(serviceurl)
data = uh.read()


stuff = json.loads(str(data))
info = stuff["comments"]

print 'User count:', len(info)

total = 0

for item in info:
    print item["count"]
    total += int(item["count"])

print total