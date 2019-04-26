// ES5 for loop
var numbers = [1, 2, 3];
var doubleNumbers = [];
for (var i = 0; i < numbers.length; i++) {
    doubleNumbers.push(numbers[i] * 2);
}
console.log(doubleNumbers);


// ES6+
const numbers2 = [1, 2, 3, 4];
const doubleNumbers2 = numbers2.map(number => number * 2);
console.log(doubleNumbers2);


const pluck = (array, property) => {
    return array.map(e => {
        return e[property];
    });
};

const paints = [
    {color: 'red'},
    {color: 'blue'},
    {color: 'white'},
    {smell: 'ughh'},
];


console.log(pluck(paints, 'color'));
console.log(pluck(paints, 'smell'));