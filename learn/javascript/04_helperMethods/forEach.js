// ES5 for loop
var colors = ['red', 'blue', 'green'];

for (var i = 0; i < colors.length; i++) {
    console.log(colors[i]);
}

// ES6+
const colors2 = ['red', 'blue', 'green'];

colors2.forEach((color => console.log(color)));

