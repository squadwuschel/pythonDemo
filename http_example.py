# haben wir vorher installiert mit 'pip3 install requests'
import requests

response = requests.get("http://api.open-notify.org/astros.json")
if(int(response.status_code) != 200):
    print("Error: " + str(response.status_code))
    exit()
     
responseJson = response.json();

print (f"People in space: {responseJson.get('number')}")

for person in  responseJson["people"]:
    print(f"{person['name']} is in {person['craft']}" )
