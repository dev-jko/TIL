package com.example.helloworld

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import kotlinx.android.synthetic.main.activity_main.*
import java.security.AccessController.getContext

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        main_button1.setOnClickListener {
            val intent = Intent(this, Main2Activity::class.java)
            startActivity(intent)
        }

        main_button2.setOnClickListener {
            if (main_textView.text == "Change Text 123123123") {
                main_textView.text = "Change2222"
            } else {
                main_textView.text = "Change Text 123123123"
            }
        }

        main_button3.setOnClickListener {
            main_textView.text = main_editText.text
        }

    }
}
