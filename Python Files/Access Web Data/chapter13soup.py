import urllib
from BeautifulSoup import *
import re


#url = raw_input('Enter - ')
html = urllib.urlopen("http://python-data.dr-chuck.net/comments_298762.html").read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('tr')
sumLIST = list()

for tag in tags:
	#print tag.("span", class_="comments").text
	#tag.findAll(text)
	#print tag.text
	#print tag.getText()
	#print tag.text
	number = re.findall("[0-9]+", tag.text)
	print number
	if number == []:
		continue
	else: 
		asciiNUM = number[0].encode("ascii")
		final = int(asciiNUM)
		sumLIST.append(final)

	
    

total = sum(sumLIST)
print total

