import string
import requests
from requests.auth import HTTPBasicAuth
import json
URL= "https://test.wikidata.org/w/api.php"
mysession=requests.Session()

user,passw="SubaPanneer","Suba@oa1u8c7lbu0dgkd38d4ijl0dh2veh9bs"

options={"action":"query","meta":"tokens","type":"login","format":"json"}
r=mysession.get(URL,params=options)
r.encoding='utf-8'
data=r.json()
if(r.status_code==200):
    csrf=data['query']['tokens']['logintoken']
    print(csrf)

options_1={"lgname": user,"lgpassword": passw,"lgtoken": csrf,"action":"login","format":"json"}
r=mysession.post(URL,data=options_1)
r.encoding='utf-8'
data1=r.json()
cookie=json.dumps(r.cookies.get_dict())
print(data1)
logintoken=data['query']['tokens']['logintoken']

option_2={"action":"query","meta":"tokens","format":"json"}
r=mysession.post(URL,data=option_2)
r.encoding='utf-8'
data2=r.json()
CSRF_TOKEN=data2['query']['tokens']['csrftoken']
print(data2)

#Create item & create claim
#To create item
entity={"labels":{"ta":{"language":"ta","value":"சண்முகம்"}},"descriptions":{"ta":{"language":"ta","value":"தங்குமிடம்"}},"datatype":"string"}
options_3={"action":"wbeditentity","new":"item","data":json.dumps(entity), "format":"json","token":CSRF_TOKEN}
#response
{'entity': {'type': 'item', 'id': 'Q232482', 'labels': {'ta': {'language': 'ta', 'value': 'சண்முகம்'}}, 'descriptions': {'ta': {'language': 'ta', 'value': 'தங்குமிடம்'}}, 'aliases': {}, 'claims': {}, 'sitelinks': {}, 'lastrevid': 655882}, 'success': 1}

#To create new property. ensure right Property
value=json.dumps({'time': '+2022-02-19T00:00:00Z', 'before': 0, 'after': 0, 'timezone': 0, 'precision': 11, 'calendarmodel': 'http://www.wikidata.org/entity/Q1985727'})
options_3={'action':'wbcreateclaim','entity':'Q232482','snaktype':'value', 'property': 'P97013','value': value, 'format':'json','token':CSRF_TOKEN, 'bot':1}
#Error will occur when invalid property or invalid value type

r = mysession.post(URL, data=options_3)
r.encoding = 'utf-8'
data3=r.json()
print(data3)