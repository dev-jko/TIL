package com.example.daggerexample

import dagger.Component
import dagger.android.AndroidInjector
import dagger.android.support.AndroidSupportInjectionModule
import javax.inject.Singleton


@Singleton
@Component(modules = {
    AndroidSupportInjectionModule::class.java,
    ActivityBindingModule::class.java,
    ApplicationModule::class.java
})
interface ApplicationComponent : AndroidInjector<BaseApplication> {

    @Component.Builder
    interface Builder {
        @BindsInstatnce
        fun application(Application application): AppComponent.Builder

        fun build(): AppComponent
    }
}