function addAll(a, b, c, d, e, f) {
    const numbers = [a, b, c, d, e, f];
    let sum = 0;
    for (const number of numbers) {
        sum += number;
    }
    return sum;
}

function addAll2(...numbers) {
    let sum = 0;
    for (const number of numbers) {
        sum += number;
    }
    return sum;
}

console.log(addAll(1, 2, 3, 4, 5, 65), addAll2(1, 2, 3, 4, 5, 65));

const a1 = [1, 2, 3, 4];
const a2 = [5, 6, 7, 8];
const a3 = a1 + a2;
const a4 = [...a1, ...a2];
console.log(a1, a2, a3, a4);

