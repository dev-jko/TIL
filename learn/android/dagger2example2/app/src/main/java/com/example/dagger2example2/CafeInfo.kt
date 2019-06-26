package com.example.dagger2example2

class CafeInfo() {

    private lateinit var name: String

    constructor(name: String) : this() {
        this.name = name
    }

    fun welcome(){
        println("Welcome $name")
    }

}