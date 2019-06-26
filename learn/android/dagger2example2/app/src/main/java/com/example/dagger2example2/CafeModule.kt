package com.example.dagger2example2

import dagger.Module
import dagger.Provides
import javax.inject.Singleton


@Module(subcomponents = [CoffeeComponent::class])
class CafeModule {

    @Singleton
    @Provides
    fun provideCafeInfo(): CafeInfo {
        return CafeInfo()
    }

    @Provides
    fun provideCoffeeMaker(heater: Heater, pump: Pump): CoffeeMaker {
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
}
