package com.nadarm.firstmac

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.navigation.fragment.findNavController
import kotlinx.android.synthetic.main.activity_main2.*

class Main2Activity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main2)
        println("${this.javaClass.simpleName} - onCreate")

        btn1.setOnClickListener {
            println("${this.javaClass.simpleName} - btn1 clicked")
            navHostFragment.findNavController().navigate(R.id.actionBlank1Fragment)
        }

        btn2.setOnClickListener {
            println("${this.javaClass.simpleName} - btn2 clicked")
            navHostFragment.findNavController().navigate(R.id.actionBlank2Fragment)
        }
    }


    override fun onStart() {
        super.onStart()
        println("${this.javaClass.simpleName} - onStart")
    }

    override fun onResume() {
        super.onResume()
        println("${this.javaClass.simpleName} - onResume")
    }

    override fun onPause() {
        super.onPause()
        println("${this.javaClass.simpleName} - onPause")
    }

    override fun onStop() {
        super.onStop()
        println("${this.javaClass.simpleName} - onStop")
    }

    override fun onDestroy() {
        super.onDestroy()
        println("${this.javaClass.simpleName} - onDestroy")
    }
}
