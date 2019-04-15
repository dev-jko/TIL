package com.example.helloworld

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.CheckBox
import android.widget.TextView

class Main2Activity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main2)
        val textView = findViewById<TextView>(R.id.myText)
        textView.text = "Hello World textView change"


    }


}
