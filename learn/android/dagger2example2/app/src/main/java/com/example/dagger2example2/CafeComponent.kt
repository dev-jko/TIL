package com.example.dagger2example2

import dagger.Component
import javax.inject.Singleton

@Singleton
@Component(modules = [CafeModule::class])
interface CafeComponent {
    fun cafeInfo(): CafeInfo

    fun coffeeMaker(): CoffeeMaker

    fun coffeeComponent(): CoffeeComponent.Builder
}