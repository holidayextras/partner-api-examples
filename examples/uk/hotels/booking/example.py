import requests

url = "https://api.holidayextras.co.uk/v1/hotel/LHRMEA"

payload = "ABTANumber=YourABTANumber&Password=YourPassword&key=YourKey&token=YourToken&ArrivalDate=2018-12-01&Nights=1&RoomCode=DBL&ParkingDays=0&Adults=2&Children=0&Title=Mr&Initial=T&Surname=TEST&Address%20%5B0%5D=1%20Test%20Street&Town=Testville&County=Testshire&Postcode=TE1%20STS&DayPhone=01234567890&Email=test%40test.com&DataProtection=N&PriceCheckFlag=Y&PriceCheckPrice=55.00"
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)