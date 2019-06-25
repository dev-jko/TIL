package com.example.daggerexample

import android.app.Application
import dagger.Module
import dagger.Provides

@Module
class ApplicationModule {

    @Provides
    fun providesContext(application: Application): providesContext {
        return application
    }
}