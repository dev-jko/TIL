const utility = require('./utility');

const accountA = 100;
const accountB = 200;
const accountC = 400;
const total = utility.addAll([accountA, accountB, accountC]);
console.log(total);
console.log(utility.name);
console.log(utility.phoneNumber);