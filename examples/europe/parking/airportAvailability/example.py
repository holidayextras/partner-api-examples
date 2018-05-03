import requests

url = "https://api.holidayextras.co.uk/v1/carpark/MUC"

querystring = {"ABTANumber":"YourABTANumber","Password":"YourPassword","ArrivalDate":"2018-06-22","DepartDate":"2018-06-29","system":"ABG","ArrivalTime":"1200","DepartTime":"1200","NumberOfPax":"1","Initials":"YourInitials","key":"YourKey","token":"YourToken"}

response = requests.request("GET", url, params=querystring)

print(response.text)