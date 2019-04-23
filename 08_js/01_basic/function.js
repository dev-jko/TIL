function add(num1, num2) {
    return num1 + num2;
}

const add2 = function (num1, num2) {
    return num1 + num2;
};

const add3 = (num1, num2) => {
    return num1 + num2;
};

// 인자가 1개라면 () 생략 가능
// 함수 코드가 return 한줄이라면 {} 생략 가능
const square = num => num * num;

console.log(square(2));

const noArgs = () => {
    return 'nothing';
};

const noArgs2 = () => 'nothing';

const manArgs = (a, b, c, d) => 'many';


function sayHello(name = 'ssafy') {
    return `hi ${name}!`;
}

const s = (n = 'ssafy') => `hi ${n}!`;

console.log(s('fafa'));
console.log(s());


console.log((num => num ** 2)(4));

