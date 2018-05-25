var request = require("request");

var options = { method: 'POST',
  url: 'https://api.holidayextras.co.uk/v1/hotel/LHRMEA',
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  form:
   { ABTANumber: 'YourABTANumber',
     Password: 'YourPassword',
     key: 'YourKey',
     token: 'YourToken',
     ArrivalDate: '2018-12-01',
     Nights: '1',
     RoomCode: 'DBL',
     ParkingDays: '0',
     Adults: '2',
     Children: '0',
     Title: 'Mr',
     Initial: 'T',
     Surname: 'TEST',
     'Address [0]': '1 Test Street',
     Town: 'Testville',
     County: 'Testshire',
     Postcode: 'TE1 STS',
     DayPhone: '01234567890',
     Email: 'test@test.com',
     DataProtection: 'N',
     PriceCheckFlag: 'Y',
     PriceCheckPrice: '55.00' } };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
