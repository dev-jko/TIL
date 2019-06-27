package com.example.dagger2example2.component

import com.example.dagger2example2.CoffeeMaker
import com.example.dagger2example2.module.CoffeeModule
import dagger.Component

@Component(modules = [CoffeeModule::class])
interface CoffeeComponent {

    fun coffeeMaker(): CoffeeMaker


}