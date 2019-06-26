package com.example.dagger2example2

class A_Heater : Heater {

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