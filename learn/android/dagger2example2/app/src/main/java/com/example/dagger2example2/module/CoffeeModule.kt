package com.example.dagger2example2.module

import com.example.dagger2example2.*
import dagger.Binds
import dagger.Module
import dagger.Provides

@Module
abstract class CoffeeModule {

    @Binds
    abstract fun heater(heater: A_Heater): Heater

    @Binds
    abstract fun pump(pump: A_Pump): Pump

    companion object {

        @Provides
        fun provideCoffeeMaker(): CoffeeMaker {
            return CoffeeMaker()
        }

    }

}