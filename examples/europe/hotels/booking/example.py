import requests

url = "https://api.holidayextras.co.uk/sandbox/v1/hotel/MUCLAN"

payload = {
  "ABTANumber": "YourABTANumber",
  "Password": "YourPassword",
  "key": "YourKey",
  "token": "YourToken",
  "ArrivalDate": "2017-12-01",
  "Nights": "1",
  "RoomCode": "DBL",
  "ParkingDays": "0",
  "Adults": "2",
  "Children": "0",
  "Title": "Mr",
  "Initial": "T",
  "Surname": "TEST",
  "Address": [ "1 Test Street" ],
  "Town": "Testville",
  "County": "Testshire",
  "Postcode": "TE1 STS",
  "DayPhone": "01234567890",
  "Email": "test@test.com",
  "DataProtection": "N",
  "System": "ABG",
  "PriceCheckFlag": "Y",
  "PriceCheckPrice": "20.00"
}
headers = {"Content-Type": "application/x-www-form-urlencoded"}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)