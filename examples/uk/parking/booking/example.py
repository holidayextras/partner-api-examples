import requests

url = "https://api.holidayextras.co.uk/v1/carpark/LGW4"

payload = "ABTANumber=YourABTANumber&Password=YourPassword&Initials=YourInitials&key=YourKey&token=YourToken&ArrivalDate=2018-12-02&ArrivalTime=1200&DepartDate=2018-12-03&DepartTime=1200&NumberOfPax=1&Title=MR&Initial=T&Surname=TEST&Address%5B%5D=123%20Test%20Street&Town=Testville&County=Testshire&PostCode=TE12%203ST&Email=test%40test.com&PriceCheckFlag=Y&PriceCheckPrice=57.99&CarColour=White&CarMake=Range%20Rover&CarModel=Evoque&Destination=Munich&OutFlight=EZY8985&OutTerminal=N&Registration=TE17%20STS&ReturnFlight=EZY8982&ReturnTerminal=N&MobileNum=01234567890"
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)