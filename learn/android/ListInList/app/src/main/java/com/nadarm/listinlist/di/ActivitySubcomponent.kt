package com.nadarm.listinlist.di

import com.nadarm.listinlist.ui.MainActivity
import dagger.Subcomponent
import dagger.android.AndroidInjector

@Subcomponent
interface ActivitySubcomponent : AndroidInjector<MainActivity> {

    @Subcomponent.Factory
    interface Factory : AndroidInjector.Factory<MainActivity>

}