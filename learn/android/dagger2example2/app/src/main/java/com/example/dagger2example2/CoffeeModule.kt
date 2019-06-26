package com.example.dagger2example2

import dagger.Module
import dagger.Provides


@Module
class CoffeeModule {

    @Provides
    fun proviedCoffeeMaker(heater: Heater, pump: Pump): CoffeeMaker {
        return CoffeeMaker(heater, pump)
    }

    @Provides
    fun provideHeater(): Heater {
        return A_Heater()
    }

    @Provides
    fun providePump(heater: Heater): Pump {
        return A_Pump(heater)
    }

    @Provides
    fun provideCoffeeBean(): CoffeeBean {
        return CoffeeBean()
    }

}
