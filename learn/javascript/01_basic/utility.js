// function addAll(numbers = []) {
//     let sum = 0;
//     numbers.forEach(number => sum += number);
//     return sum;
// }
//
// function subAll() {
//
// }

// module.exports = {
//     addAll,
//     subAll
// };
// module.exports = {
//     addAll: addAll,
//     subAll: subAll
// };

module.exports = {
    addAll(numbers = []) {
        let sum = 0;
        numbers.forEach(number => sum += number);
        return sum;
    },
    subAll() {

    },
    name: 'neo'
};

module.exports.phoneNumber = '010123456';