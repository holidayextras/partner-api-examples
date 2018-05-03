var request = require("request");

var options = { method: 'POST',
  url: 'https://api.holidayextras.co.uk/v1/carpark/LGW4',
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  form:
   { ABTANumber: 'YourABTANumber',
     Password: 'YourPassword',
     Initials: 'YourInitials',
     key: 'YourKey',
     token: 'YourToken',
     ArrivalDate: '2018-12-02',
     ArrivalTime: '1200',
     DepartDate: '2018-12-03',
     DepartTime: '1200',
     NumberOfPax: '1',
     Title: 'MR',
     Initial: 'T',
     Surname: 'TEST',
     'Address[]': '123 Test Street',
     Town: 'Testville',
     County: 'Testshire',
     PostCode: 'TE12 3ST',
     Email: 'test@test.com',
     PriceCheckFlag: 'Y',
     PriceCheckPrice: '57.99',
     CarColour: 'White',
     CarMake: 'Range Rover',
     CarModel: 'Evoque',
     Destination: 'Munich',
     OutFlight: 'EZY8985',
     OutTerminal: 'N',
     Registration: 'TE17 STS',
     ReturnFlight: 'EZY8982',
     ReturnTerminal: 'N',
     MobileNum: '01234567890' } };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
