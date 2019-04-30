function makeCoffee(order, serve) {
    let cup;
    setTimeout(() => {
        cup = order;
        serve(cup);
    }, 2000);
}


makeCoffee('latte', console.log);
