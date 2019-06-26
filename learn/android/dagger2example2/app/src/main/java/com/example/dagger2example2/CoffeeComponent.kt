package com.example.dagger2example2

import dagger.Subcomponent

@Subcomponent(modules = [CoffeeModule::class])
interface CoffeeComponent {

    fun coffeeMaker(): CoffeeMaker

    fun coffeeBean(): CoffeeBean

    fun inject(coffeeMaker: CoffeeMaker)

    @Subcomponent.Builder
    interface Builder {
        fun build(): CoffeeComponent
    }
}