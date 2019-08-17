package com.nadarm.androidcomponentexample

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        buttonStart.setOnClickListener {
            val intent = Intent(this, MyService::class.java)
            startService(intent)
        }

        buttonEnd.setOnClickListener {

        }




        buttonStart2.setOnClickListener {
            val intent = Intent(this, MyIntentService::class.java)
            startService(intent)
        }

        buttonEnd2.setOnClickListener {

        }


    }
}
