var request = require("request");

var options = { method: 'POST',
  url: 'https://api.holidayextras.co.uk/v1/lounge/HAMLHL',
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  form:
   { ABTANumber: 'YourABTANumber',
     Password: 'YourPassword',
     Initials: 'YourInitials',
     key: 'YourKey',
     token: 'YourToken',
     ArrivalDate: '2018-12-12',
     ArrivalTime: '1200',
     Adults: '2',
     Title: 'MR',
     Initial: 'T',
     Surname: 'TEST',
     'Address[]': '123 Test Street',
     Town: 'Testville',
     County: 'Testshire',
     PostCode: 'TE12 3ST',
     Email: 'test@test.com',
     PriceCheckFlag: 'Y',
     PriceCheckPrice: '70.00',
     MobileNum: '01234567890',
     Children: '0',
     System: 'ABG' } };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
