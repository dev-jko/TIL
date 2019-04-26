// ES5 for loop

var products = [
    {name: 'cucumber', type: 'vege'},
    {name: 'banana', type: 'fruit'},
    {name: 'carrot', type: 'vege'},
    {name: 'tomato', type: 'fruit'},
];
var fruits = [];
for (var i = 0; i < products.length; i++) {
    if (products[i].type === 'fruit') {
        fruits.push(products[i]);
    }
}
console.log(fruits);


// ES6+

const products2 = [
    {name: 'cucumber', type: 'vege'},
    {name: 'banana', type: 'fruit'},
    {name: 'carrot', type: 'vege'},
    {name: 'tomato', type: 'fruit'},
];
const veges = products2.filter(product => {
    return product.type === 'vege'
});
console.log(veges);


const users = [
    {id: 1, admin: true},
    {id: 2, admin: false},
    {id: 3, admin: false},
    {id: 4, admin: true},
    {id: 5, admin: false},
];

const adminUsers = users.filter(user => user.admin);
console.log(adminUsers);








