import HTMLParser
import urllib
import sys,re
import string,glob
url='/tftpboot/python/second/*.html'
for filename in glob.glob(url):
	web=urllib.urlopen(filename).read()
	web=string.replace(str(web),"play.php","loadfile.php")
	link=re.findall('<a href="([^><]+)"',str(web))
	title=re.findall('>([^><]+)</a>',str(web))
        #print link
	#print title
	i=0
	while i<len(link):
		link[i]=str(link[i])
		title[i]=title[i].decode('gb2312')
		urllib.urlretrieve(link[i],'/tftpboot/python/second'+'/'+title[i])
		i+=1
