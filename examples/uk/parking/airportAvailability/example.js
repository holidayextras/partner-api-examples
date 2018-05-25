var request = require("request");

var options = { method: 'GET',
  url: 'https://api.holidayextras.co.uk/carpark/LGW',
  qs:
   { ABTANumber: 'YourABTANumber',
     Password: 'YourPassword',
     Initials: 'YourInitials',
     key: 'YourKey',
     token: 'YourToken',
     ArrivalDate: '2018-12-01',
     ArrivalTime: '1200',
     DepartDate: '2018-12-08',
     DepartTime: '1200',
     NumberOfPax: '1' },
  };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
