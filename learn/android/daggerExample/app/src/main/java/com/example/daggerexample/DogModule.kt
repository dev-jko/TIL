package com.example.daggerexample

import dagger.Module
import dagger.Provides

@Module
object DogModule {

    @Provides
    fun provideDog(): Dog {
        return Dog()
    }
}