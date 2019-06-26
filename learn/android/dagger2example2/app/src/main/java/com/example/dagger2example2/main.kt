package com.example.dagger2example2

fun main() {

//    val coffeeMaker: CoffeeMaker = Injection.provideCoffeeMaker()
//    coffeeMaker.brew()


    DaggerCoffeeComponent.create().make().brew()


    val cafeComponent: CafeComponent = DaggerCafeComponent.create()
    val cafeInfo1 = cafeComponent.cafeInfo()
    val cafeInfo2 = cafeComponent.cafeInfo()
    println("$cafeInfo1, $cafeInfo2, ${cafeInfo1 == cafeInfo2}")

    val coffeeComponent: CoffeeComponent = DaggerCoffeeComponent.create()
    val coffeeMaker1 = coffeeComponent.make()
    val coffeeMaker2 = coffeeComponent.make()
    println("$coffeeMaker1, $coffeeMaker2, ${coffeeMaker1 == coffeeMaker2}")

}