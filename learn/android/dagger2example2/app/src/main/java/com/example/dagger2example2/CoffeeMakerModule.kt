package com.example.dagger2example2

import dagger.Module
import dagger.Provides

@Module
class CoffeeMakerModule {

    @Provides
    fun provideHeater():Heater{
        return A_Heater()
    }

    @Provides
    fun providePump(heater: Heater):Pump{
        return A_Pump(heater)
    }
}