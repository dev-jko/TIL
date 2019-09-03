package com.nadarm.listinlist.di

import android.app.Application
import dagger.Component
import javax.inject.Singleton

@Singleton
@Component(modules = [MainActivityModule::class])
interface AppComponent {

    fun inject(app: Application)

}