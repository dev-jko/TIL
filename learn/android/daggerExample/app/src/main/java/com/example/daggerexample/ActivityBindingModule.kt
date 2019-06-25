package com.example.daggerexample

import android.app.ActivityManager
import dagger.Module
import dagger.android.ContributesAndroidInjector

@Module
abstract class ActivityBindingModule {
    @ActivityScoped
    @ContributesAndroidInjector(modules = TasksModule::class)
    abstract fun tasksActivity():TasksActivity

    @ActivityScoped
    @ContributesAndroidInjector(modules = TaskDetailPresenterModule::class)
    abstract fun taskDetailActivity():TaskDetailActivity
}