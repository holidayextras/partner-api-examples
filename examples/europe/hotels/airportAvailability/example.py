import requests

url = "https://api.holidayextras.co.uk/v1/hotel/MUC"

querystring = {"ABTANumber":"YourABTANumber","Password":"YourPassword","key":"YourPassword","token":"YourToken","ArrivalDate":"2018-12-01","Nights":"1","RoomType":"D20","ParkingDays":"0","System":"ABG","lang":"de"}

response = requests.request("GET", url, params=querystring)

print(response.text)