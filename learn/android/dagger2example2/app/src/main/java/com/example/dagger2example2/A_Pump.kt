package com.example.dagger2example2

class A_Pump(private val heater: Heater): Pump {

    override fun pump() {
        if (heater.isHot()) {
            println("A_Pump : pumping")
        }
    }
}