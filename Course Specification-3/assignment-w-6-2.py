import urllib.request,urllib.error,urllib.parse
import json
import ssl
api_key=42
serviceurl='http://py4e-data.dr-chuck.net/json?'

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode= ssl.CERT_NONE
address= input("LOCATION: ")
parms=dict()
parms['address']=address
parms['key']=api_key
url= serviceurl+ urllib.parse.urlencode(parms)

print("Retrieving Url:",url)
uh= urllib.request.urlopen(url,context=ctx)
data=uh.read().decode()

print("Retrieved:::::::\n")

try:
	js=json.loads(data)
except :
	js=None
	if not js or 'status' not in js or js['status']!="OK":
		print('---Failed to retrieve---')
		print(data)
		exit()
print(json.dumps(js,indent=3))

print(js['results'][0]['place_id'])

