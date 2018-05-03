var request = require("request");

var options = { method: 'GET',
  url: 'https://api.holidayextras.co.uk/v1/carpark/MUC',
  qs:
   { ABTANumber: 'YourABTANumber',
     Password: 'YourPassword',
     ArrivalDate: '2018-06-22',
     DepartDate: '2018-06-29',
     system: 'ABG',
     ArrivalTime: '1200',
     DepartTime: '1200',
     NumberOfPax: '1',
     Initials: 'YourInitials',
     key: 'YourKey',
     token: 'YourToken' } };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
