function waitNSeconds(n) {
    return new Promise(((resolve, reject) => {
        setTimeout(() => {
            console.log(`${n} second(s) passed`);
            resolve()
        }, n * 1000)
    }));
}

function waitFor10Seconds() {
    waitNSeconds(1)
        .then(() => waitNSeconds(2))
        .then(() => waitNSeconds(3))
        .then(() => waitNSeconds(4))
        .then(() => console.log('Total 10 seconds!'));
}

async function waitFor10Seconds2() {
    await waitNSeconds(1);
    await waitNSeconds(2);
    await waitNSeconds(3);
    await waitNSeconds(4);
    console.log('Total 10 seconds!');
}


waitFor10Seconds2();