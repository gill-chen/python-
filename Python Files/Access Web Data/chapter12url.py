import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
#html = urllib.urlopen("http://python-data.dr-chuck.net/known_by_Siyona.html").read()
#soup = BeautifulSoup(html)
url = "http://python-data.dr-chuck.net/known_by_Siyona.html"
# Retrieve all of the anchor tags
for i in range(0,7):
	
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	count = 1
	for tag in tags:
	    #print tag.get('href', None)
	    
	    if count == 18:
	    	url = tag.get('href', None)
	    	print url
	    	break
	    else:
	    	count += 1
	    	