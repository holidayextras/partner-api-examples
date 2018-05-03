var request = require("request");

var options = { method: 'GET',
  url: 'https://api.holidayextras.co.uk/v1/lounge/HAM',
  qs:
   { ABTANumber: 'YourABTANumber',
     Password: 'YourPassword',
     Initials: 'YourInitials',
     key: 'YourKey',
     token: 'YourToken',
     ArrivalDate: '2018-12-01',
     ArrivalTime: '1200',
     Adults: '2',
     Children: '0',
     System: 'ABG' } };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
