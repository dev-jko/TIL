function hi() {

}

const bye = () => {

};


const me = {
    name: 'kjd',
    phone: '01012341234',
    intro: function () {
        return `hi my name is ${this.name}.`
    }
};


const you = {
    name: 'you',
    phone: '01012341234',
    intro: () => {
        return `hi my name is ${this.name}.`
    }
};


console.log(me.intro());
console.log(you.intro());