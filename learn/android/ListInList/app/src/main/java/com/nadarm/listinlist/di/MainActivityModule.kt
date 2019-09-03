package com.nadarm.listinlist.di

import com.nadarm.listinlist.ui.MainActivity
import dagger.Binds
import dagger.Module
import dagger.android.AndroidInjector
import dagger.multibindings.ClassKey
import dagger.multibindings.IntoMap

@Module(subcomponents = [ActivitySubComponent::class])
abstract class MainActivityModule {

    @Binds
    @IntoMap
    @ClassKey(MainActivity::class)
    abstract fun bindAndroidInjectorFectory(factory: ActivitySubComponent.Factory): AndroidInjector.Factory<out Any>

}
