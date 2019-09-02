package com.nadarm.listinlist.di

import android.app.Application
import dagger.Module
import dagger.Provides
import javax.inject.Singleton

@Module
object AndroidApp : Application() {

    val appComponent: AppComponent = DaggerAppComponent.builder().build()

    @Singleton
    @JvmStatic
    @Provides
    fun provideApplication(): Application = this
}