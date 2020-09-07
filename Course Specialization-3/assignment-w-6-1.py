import json
import urllib.request, urllib.parse,urllib.error

url=input()
print("retrieving url: ",url)
uh=urllib.request.urlopen(url)
data=uh.read().decode()

try:
	js=json.loads(data)
except :
	js=None
	if not js or 'status' not in js or js['status']!="OK":
		print('---Failed to retrieve---')
		print(data)
		exit()
print(json.dumps(js,indent=2))
lst=list()
for cm in js['comments']:
	count=int(cm['count'])
	lst.append(count)
print(sum(lst))