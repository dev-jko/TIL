package com.example.daggerexample

import dagger.Module
import dagger.Provides

@Module
object CatModule {

    @Provides
    fun provideCat(): Cat {
        return Cat()
    }
}