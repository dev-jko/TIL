package com.example.dagger2example2

import javax.inject.Inject

class A_Pump @Inject constructor(private val heater: Heater) : Pump {

    override fun pump() {
        if (heater.isHot()) {
            println("A_Pump : pumping")
        }
    }
}