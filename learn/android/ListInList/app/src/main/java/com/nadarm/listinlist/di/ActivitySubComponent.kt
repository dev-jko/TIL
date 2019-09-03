package com.nadarm.listinlist.di

import com.nadarm.listinlist.data.DataProvideModule
import com.nadarm.listinlist.ui.MainActivity
import dagger.Subcomponent
import dagger.android.AndroidInjector

@Subcomponent(modules = [DataProvideModule::class])
interface ActivitySubComponent : AndroidInjector<MainActivity> {

    @Subcomponent.Factory
    interface Factory : AndroidInjector.Factory<MainActivity>


}