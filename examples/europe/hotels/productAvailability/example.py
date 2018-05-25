import requests

url = "https://api.holidayextras.co.uk/v1/hotel/MUCLAN"

querystring = {"ABTANumber":"YourABTANumber","Password":"YourPassword","key":"YourKey","token":"YourToken","ArrivalDate":"2018-12-01","Nights":"1","RoomType":"D20","ParkingDays":"8","System":"ABG"}

response = requests.request("GET", url, params=querystring)

print(response.text)