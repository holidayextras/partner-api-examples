import requests

url = "https://api.holidayextras.co.uk/carpark/MU01"

payload = {
  "ABTANumber": "YourABTANumber",
  "Password": "YourPassword",
  "Initials": "YourInitials",
  "key": "YourKey",
  "token": "YourToken",
  "ArrivalDate": "2018-12-01",
  "ArrivalTime": "1200",
  "DepartDate": "2018-12-08",
  "DepartTime": "1200",
  "NumberOfPax": "1",
  "Title": "MR",
  "Initial": "T",
  "Surname": "TEST",
  "Address": [ "123 Test Street" ],
  "Town": "Testville",
  "County": "Testshire",
  "PostCode": "TE12 3ST",
  "Email": "test@test.com",
  "PriceCheckFlag": "Y",
  "PriceCheckPrice": "57.99",
  "System": "ABG",
  "OutFltNo": "EZY8982",
  "InFltNo": "EZY8985",
  "InFltTime": "1130"
  }
headers = {"Content-Type": "application/x-www-form-urlencoded"}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)