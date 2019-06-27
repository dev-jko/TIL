package com.example.dagger2example2

import javax.inject.Inject

class CoffeeMaker
@Inject constructor(
    private val heater: Heater,
    private val pump: Pump
) {
    fun brew(coffeeBean: CoffeeBean) {
        heater.on()
        pump.pump()
        println(coffeeBean)
        println(" [_]P coffee! [_]P ")
        heater.off()
    }
}