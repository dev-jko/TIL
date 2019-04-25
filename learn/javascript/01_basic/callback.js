const numbersEachAdd = numbers => {
    let acc = 0;
    for (const number of numbers) {
        acc += number;
    }
    return acc;
};

// console.log(numbersEachAdd([1, 2, 3, 4, 5]));


const numbersEachSub = numbers => {
    let acc = 0;
    for (number of numbers) {
        acc -= number;
    }
    return acc;
};

// console.log(numbersEachSub([1, 2, 3, 4, 5]));


const numberEach = (numbers, callback) => {
    let acc;
    for (const number of numbers) {
        acc = callback(number, acc);
    }
    return acc;
};


const adder = (number, sum = 0) => number + sum;
// const adder = (number, acc) => number - acc;
// const adder = (number, acc) => number * acc;
// const adder = (number, acc) => number / acc;

console.log(numberEach([1, 2, 3, 4, 5], adder));
console.log(numberEach([1, 2, 3, 4, 5], (n, sub = 0) => sub - n));
console.log(numberEach([1, 2, 3], (n, mul = 1) => mul * n));



