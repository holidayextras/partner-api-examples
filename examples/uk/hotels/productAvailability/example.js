var request = require("request");

var options = { method: 'GET',
  url: 'https://api.holidayextras.co.uk/v1/hotel/LHRHIL',
  qs:
   { ABTANumber: 'YourABTANumber',
     Password: 'YourPassword',
     key: 'YourKey',
     token: 'YourToken',
     ArrivalDate: '2018-12-01',
     Nights: '1',
     RoomType: 'D20',
     ParkingDays: '0' } };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
