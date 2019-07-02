package com.example.koinexample

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import org.koin.android.ext.android.get

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val service: BusinessService = get()
    }
}
