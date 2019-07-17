import urllib2
import re
import sys

program_name = sys.argv[0]
url = sys.argv[1]
print("\033[1;36m URL: \033[1;00m"+url)
try:
    html_content = urllib2.urlopen(url).read()
    matches = re.findall('AIza[0-9A-Za-z\\-_]{35}', html_content);
    #quit() if matches == 0


except:
       print("\033[1;31m Status : Not Working \033[1;00m")
       quit()


for i in matches:
      urlm = "https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key="
      mapurl=urlm+i
      vul = urllib2.urlopen(mapurl).read()
      vulmatch = re.findall('error_message',vul)
      if len(vulmatch) == 0 :
         vulmatch="Vulnerable"
      else :
         vulmatch="Not Vulnerable"
      print("\033[1;32m"+i+"\033[1;00m"+ vulmatch)
      f=open("abc.txt","a+")
      f.write(url+":"+i+ ":" +vulmatch+ "\n")

