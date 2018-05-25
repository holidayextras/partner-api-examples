import requests

url = "https://api.holidayextras.co.uk/carpark/LHH6"

querystring = {"ABTANumber":"YourABTANumber","Password":"YourPassword","Initials":"YourInitials","key":"YourKey","token":"YourToken","ArrivalDate":"2017-12-01","ArrivalTime":"1200","DepartDate":"2017-12-08","DepartTime":"1200","NumberOfPax":"1"}

response = requests.request("GET", url, params=querystring)

print(response.text)