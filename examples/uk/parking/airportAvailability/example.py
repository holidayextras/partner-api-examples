import requests

url = "https://api.holidayextras.co.uk/carpark/LGW"

querystring = {"ABTANumber":"YourABTANumber","Password":"YourPassword","Initials":"YourInitials","key":"YourKey","token":"YourToken","ArrivalDate":"2018-12-01","ArrivalTime":"1200","DepartDate":"2018-12-08","DepartTime":"1200","NumberOfPax":"1"}

response = requests.request("GET", url, params=querystring)

print(response.text)