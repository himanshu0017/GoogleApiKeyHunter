import urllib2
import re
import sys

program_name = sys.argv[0]
url = sys.argv[1]
#url="https://sxsw.delltechnologies.com"
print("\033[1;36m URL: \033[1;00m"+url)
try:
    html_content = urllib2.urlopen(url).read()
    matches = re.findall('https://maps.googleapis.com/maps/api.*?>', html_content);
    #quit() if matches == 0


except:
       print("\033[1;31m Status : Not Working \033[1;00m")
       quit()


for i in matches:
      print("\033[1;32m"+i+"\033[1;00m")
      f=open("test.txt","a+")
      f.write(url+":"+i+"\n")
