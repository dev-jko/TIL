package com.example.dagger2example2

import javax.inject.Inject

class CafeInfo(private val name: String) {
    @Inject
    lateinit var coffeeMaker: CoffeeMaker

    @Inject
    lateinit var coffeeBean: CoffeeBean

    fun welcome() {
        println("Welcome $name")
    }

    fun brew() {
        coffeeMaker.brew(coffeeBean)
    }

}