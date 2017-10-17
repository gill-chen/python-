
# import socket

# mysock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(("www.pythonlearn.com", 80))

# mysock.send(b"GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n")

# while True:
# 	data = mysock.recv(512)
# 	if (len(data)<1):
# 		break
# 	print (data)

# mysock.close()

# import urllib.request

# fhand = urllib.urlopen("http://www.pythonlearn.com/code/intro-short.txt ")

# for line in fhand:
# 	print (line.strip())

# import urllib.request as ur

# filehandler = ur.urlopen ('http://www.pythonlearn.com/code/intro-short.txt')

# for line in filehandler:
#     print(line.strip())

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.pythonlearn.com', 80))
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()