import urllib.parse 
import requests 

main_api = "https://www.mapquestapi.com/directions/v2/route?" 
orig = "Washington, D.C." 
dest = "Baltimore, Md" 
key = "ScjKx3iErPfxrgjijjqnWf2bV1X8keCG"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})  
print("URL ",(url))
json_data = requests.get(url).json() 
print(json_data) 