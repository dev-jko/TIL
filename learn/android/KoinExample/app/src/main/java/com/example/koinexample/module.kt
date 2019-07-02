package com.example.koinexample

import org.koin.dsl.module

class Controller(val service: BusinessService) {
    fun hello() {
        service.sayHello()
    }
}

class BusinessService()

val myModule = module {
    single { Controller(get()) }
    single { BusinessService() }
}