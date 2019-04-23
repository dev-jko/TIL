// This is Comment

function concat(str1, str2) {
    return `${str1} - ${str2}`;
}

const checkLongStr = string => string.length > 10;

if (checkLongStr(concat('Happy', 'Hacking'))) {
    console.log('LONG STRING');
} else {
    console.log('SHORT STRING');
}

checkLongStr(concat('Happy', 'Hacking')) ? console.log('LONG STRING') : console.log('SHORT STRING');
