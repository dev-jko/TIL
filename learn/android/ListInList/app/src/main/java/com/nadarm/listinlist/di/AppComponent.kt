package com.nadarm.listinlist.di

import com.nadarm.listinlist.data.DataProvideModule
import dagger.Component
import javax.inject.Singleton

@Singleton
@Component(modules = [AndroidApp::class, DataProvideModule::class])
interface AppComponent {


}