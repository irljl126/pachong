import HTMLParser
import urllib
import sys,re
import string
urlString = "http://202.117.122.48"
#file=open('/tftpboot/python/index.html','r')
web = urllib.urlopen("index.html").read()
web = str(web)
link=re.findall('<a href="(.+)"',web)
title=re.findall('>([^><]+)</a>',web)
#print link
#print title
#for lin in link:
#print link[0]
i=0
#print len(link)
while i<len(link):
     web1=urllib.urlopen(link[i]).read()
     web1=str(web1)
     link1=re.findall('<a href="([^><c/]+)" target="_blank" title=',web1)#model one
     title1=re.findall('"_blank" title="([^><]+)">',web1)
     link2=re.findall('<a href="([^>_<c/]+)" title="',web1)# model two
     title2=re.findall('" title="([^><"]+)" target="',web1)
     link1=sorted(set(link1),key=link1.index)
     title1=sorted(set(title1),key=title1.index)
     link2=sorted(set(link2),key=link2.index)
     title2=sorted(set(title2),key=title2.index)
     name=title[i].decode('gb2312')# solve the problem of fault decode
     os.makedirs('/tftpboot/python/second'+'/'+name)
     #print name
     m=0
     n=0
     if i==0:
	     
             while m<len(link1):
	          file=open('/tftpboot/python/second'+'/'+name+'.html','a+')
	          file.write('<a href="' + urlString + '/' + link1[m] + '">' + title1[m] + '</a>' + '<hr />')
	          file.write('\n')
	          file.close
	          m+=1
     else:

             while n<len(link2):
	          file=open('/tftpboot/python/second'+'/'+name+'.html','a+')
                  file.write('<a href="' + urlString + '/' + link2[n] + '">' + title2[n] + '</a>' + '<hr />')
	          file.write('\n')
	          file.close()
	          n+=1
     i+=1
#print link2,
#print '/n'
#print title2
#print len(link1),len(link2),len(title1),len(title2)
#i=0
#while i<len(title):
#	print link[i]
#	file=open('/tftpboot/python/index.html','a+')
#	file.write('<a href="'+ urlString + '/' + link[i] + '">' + title[i] + '</a></li>' + '<hr />')
#	file.write('\n')
#	i+=1
#file.close()
