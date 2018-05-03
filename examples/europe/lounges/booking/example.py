import requests

url = "https://api.holidayextras.co.uk/v1/lounge/HAMLHL"

payload = "ABTANumber=YourABTANumber&Password=YourPassword&Initials=YourInitials&key=YourKey&token=YourToken&ArrivalDate=2018-12-12&ArrivalTime=1200&Adults=2&Title=MR&Initial=T&Surname=TEST&Address%5B%5D=123%20Test%20Street&Town=Testville&County=Testshire&PostCode=TE12%203ST&Email=test%40test.com&PriceCheckFlag=Y&PriceCheckPrice=70.00&MobileNum=01234567890&Children=0&System=ABG"
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)