// ES5 for loop
var avengers = [
    {name: 'Tony Stark'},
    {name: 'Steve Rogers'},
    {name: 'Thor'},
];
var avenger;
for (var i = 0; i < avengers.length; i++) {
    if (avengers[i].name === 'Tony Stark') {
        avenger = avengers[i];
        break;
    }
}
console.log(avenger);


// ES6+
const avengers2 = [
    {name: 'Tony Stark'},
    {name: 'Steve Rogers'},
    {name: 'Thor'},
];
const avenger2 = avengers2.find(e => e.name === 'Thor');
console.log(avenger2);
