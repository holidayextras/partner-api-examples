import requests

url = "https://api.holidayextras.co.uk/v1/lounge/HAM"

querystring = {"ABTANumber":"YourABTANumber","Password":"YourPassword","Initials":"YourInitials","key":"YourKey","token":"YourToken","ArrivalDate":"2018-12-01","ArrivalTime":"1200","Adults":"2","Children":"0","System":"ABG"}

response = requests.request("GET", url, params=querystring)

print(response.text)