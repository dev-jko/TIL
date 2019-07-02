package com.example.koinexample

import org.junit.Test
import org.koin.core.context.startKoin

class SimpleTest {

    val service: BusinessService by inject()

    @Test
    fun myTest() {
        startKoin { modules(myModule) }
        val service: BusinessService = get()
    }

}