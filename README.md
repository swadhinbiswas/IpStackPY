
# About Project

## Locate and Identify Website Visitors by IP Address

Ipstack Offers One of the Leading IP to Geolocation APIs and Global IP Database Services Worldwide.
This Project help you to use all the ipstack - a real-time geolocation API service using python in your CLI,Bot,Etc.

# API service

## Location Module

Use ipstack's extensive set of localization data to implement geographic restrictions on your site, optimize ad targeting or deliver user experiences customized based on the location of your website visitors


## Currency Module

Get instant and accurate information about the primary currency used in the location returned for the processed IP address and deliver a tailored shopping experience to your customers.


## Time Zone Module

Find out about the time zone your users are located in without the need for them to fill out any forms, and act accordingly based on the time-related metadata returned by the ipstack API


## Connection Module

Make use of valuable information about the ASN and the hostname of the ISP your website visitors are using.


## Security Module

Protect your site and web application and always be a step ahead of potential threats to your business by detecting proxies, crawlers or tor users at first glance.
## Authors

- [@swadhinbiswas](https://www.github.com/swadhinbiswas)




## API Reference

#### simple use
```
ipstack=IpStack(ipaddress,apikey)

```
#### all function
```
get_Apicall()
#for get call

getlocation()
# Get only Location Of IPAddress using IpStack

hostname_looku()
#for enable Description of DNS 

api_xmlformat()
#Get data in XML format

callby_function(function)
#make api call using Custom Function 

enable_security_apicall()
#enable security when call API

callby_fields(Parameter)
#call api using Parameter




```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |
| :-------- | :------- | :------------------------- |
| `ipaddress` | `string` | **Required**. Your IpAddress |
| `url` | `string` | **Required**. Your url|

#### Get item



| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |




Request Parameters:

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |
| :-------- | :------- | :------------------------- |
| `ipaddress` | `string` | **Required**. Your IpAddress |
| `url` | `string` | **Required**. Your url|
| `hostname` | `string` | [optional] Set to 1 to enable Hostname Lookup.|


# Specify Response Language
``en - English/US``

``de - German``

``es - Spanish``

``fr - French``

``ja - Japanese``

``pt-br - Portugues (Brazil)``

``ru - Russian``

``zh - Chinese``


# JSONP Callbacks

```
 def callby_function(self,function):
        urlx=f"{self.url}&callback={function}&json"
        txt=requests.get(urlx).text
        import json
        # api=json.loads(txt)
        return txt
    
```
### creat Function
#### example 
