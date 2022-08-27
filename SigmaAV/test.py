from bs4 import BeautifulSoup
import requests
print("Enter the hash value of your file: ")
hash= input("HASH: ")
print(hash)
link = "http://https://www.virustotal.com/gui/file/"+hash+"/details"
print(link)
page= requests.get(link)
contentOfPage= page.content
soup= BeautifulSoup(contentOfPage, 'html5lib')
soup= str(soup)
print(soup.find("No security vendors and no sandboxes flagged this file as malicious"))
if soup.find("No security vendors and no sandboxes flagged this file as malicious")==-1:
	print("unsafe")
else:
	print("safe")