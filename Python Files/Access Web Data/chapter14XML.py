import urllib
import xml.etree.ElementTree as ET

serviceurl = ' http://python-data.dr-chuck.net/comments_298759.xml ' 
# + urllib.urlencode({"version":"1.0", "encoding":"UTF-8"})


XML = urllib.urlopen(serviceurl)
uh = XML.read()
tree = ET.fromstring(uh)

categories = tree.find("comments")
comments = categories.find("comment")
counts = comments.find("count")


listings = tree.findall("comments/comment")
total = 0

for item in listings:
    count = item.find("count").text
    number = int(count)
    total += number

print total 
# print tree.tag
# for grandparent in tree:
#     print grandparent.tag
#     for parent in grandparent:
#         print parent.find("count").text
# listings = ET.parse(uh).findall(".//comment")

# print tree.findall("commentinfo")

# listings = tree.findall("commentinfo/comments/comment")
 
# print listings
    

# for comments in data.findall("comment"):
#     count = comments.find("count").text
#     name = comments.find("name").text
#     print count, name 


#tree = data.findall('.//{http://python-data.dr-chuck.net/comments_298759.xml}count')

# counts = data.findall(".//count")
# print counts
#for item in counts:
    #print "count", item.find("count").text