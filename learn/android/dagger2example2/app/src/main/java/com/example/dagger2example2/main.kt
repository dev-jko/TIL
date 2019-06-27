package com.example.dagger2example2

import com.example.dagger2example2.component.DaggerCoffeeComponent
import javax.inject.Inject

fun main() {

//    val coffeeMaker: CoffeeMaker = Injection.provideCoffeeMaker()
//    coffeeMaker.brew()

    val cafe = CafeInfo("my cafe")
    cafe.welcome()
    cafe.brew()

//    DaggerCoffeeComponent.create().make().brew()
//
//
//    val cafeComponent: CafeComponent = DaggerCafeComponent.create()
//    val cafeInfo1 = cafeComponent.cafeInfo()
//    val cafeInfo2 = cafeComponent.cafeInfo()
//    println("$cafeInfo1, $cafeInfo2, ${cafeInfo1 == cafeInfo2}")
//
//    val coffeeComponent: CoffeeComponent = DaggerCoffeeComponent.create()
//    val coffeeMaker1 = coffeeComponent.make()
//    val coffeeMaker2 = coffeeComponent.make()
//    println("$coffeeMaker1, $coffeeMaker2, ${coffeeMaker1 == coffeeMaker2}")

}