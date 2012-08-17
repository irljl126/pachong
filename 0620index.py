import HTMLParser
import urllib
import sys,re
import string
urlString = "http://202.117.122.48"
web = urllib.urlopen(urlString).read()
web = str(web)
#web = web[5000:10000]
#web = web.decode("gb2312").encode("utf8")
#print web
#print web.decode('gb2312').encode('utf-8')
link=re.findall('<li><a href="(.+)"',web)
title=re.findall('>([^><]+)</a></li>',web)
print link
print title
i=0
while i<len(title):
	print link[i]
	file=open('/tftpboot/python/index.html','a+')
	file.write('<a href="'+ urlString + '/' + link[i] + '">' + title[i] + '</a>' + '<hr />')
	file.write('\n')
	i+=1
file.close()

#print title[0]
