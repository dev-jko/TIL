package com.example.dagger2example2

class Injection {

    companion object {
        fun provideHeater(): Heater {
            return A_Heater()
        }

        fun providePump(): Pump {
            return A_Pump(provideHeater())
        }

        fun provideCoffeeMaker(): CoffeeMaker {
            return CoffeeMaker(provideHeater(), providePump())
        }
    }
}