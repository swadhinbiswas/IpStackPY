import requests

class IpStack():
    def __init__(self,ipaddress,apikey,*args,**kwerrgs):
        self.ipaddress=ipaddress
        self.apikey=apikey
        self.url=f"http://api.ipstack.com/{ipaddress}?access_key={apikey}&en"
        self.function=args
    
    def get_Apicall(self):
        api=requests.get(self.url).json()
        return api

    
    def getlocation(self):
        api=self.get_Apicall()
        return api["location"]
    
    def hostname_lookup(self):
        lurl=f"{self.url}&hostname=1"
        api=requests.get(lurl).json()
        return api
    
    def api_xmlformat(self):
        url_xml=f"{self.url}&output=xml"
        api=requests.get(url_xml)
        dict_data=api.content
        return dict_data
    
    def callby_function(self,function):
        urlx=f"{self.url}&callback={function}&json"
        txt=requests.get(urlx).text
        import json
        # api=json.loads(txt)
        return txt
    
    def enable_security_apicall(self):
        secureurl=f"{self.url}&security=1"
        api=requests.get(secureurl).json()
        return api
    
    def callby_fields(self,kwerrgs):
        url=f"{self.url}&fields={kwerrgs}"
        api=requests.get(url).json()
        return api