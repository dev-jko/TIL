package com.example.dagger2example2

import javax.inject.Inject

class CoffeeMaker
@Inject constructor(
    @Inject private val heater: Heater,
    @Inject private val pump: Pump
) {
    fun brew(coffeeBean: CoffeeBean) {
        heater.on()
        pump.pump()
        println(coffeeBean)
        println(" [_]P coffee! [_]P ")
        heater.off()
    }
}