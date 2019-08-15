package com.example.schedulerexample

import android.app.Application

class MyApplication:Application() {


    private val component: MyComponent = DaggerMyComponent.builder().build()

    fun getComponent(): MyComponent = this.component

}