const logEnd = () => {
    console.log('end');
};


function sleep_3s() {
    setTimeout(() => {
        console.log('wake up');
    }, 2000);
}


// console.log('start');
// setTimeout(logEnd, 2000);


console.log('start');
setTimeout(sleep_3s, 2000);
console.log('end');

