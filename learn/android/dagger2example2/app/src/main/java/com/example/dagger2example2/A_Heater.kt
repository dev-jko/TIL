package com.example.dagger2example2

import javax.inject.Inject

class A_Heater @Inject constructor() : Heater {

    private var heating: Boolean = false

    override fun on() {
        println("A_Heater : heating")
        heating = true
    }

    override fun off() {
        heating = false
    }

    override fun isHot(): Boolean {
        return heating
    }
}