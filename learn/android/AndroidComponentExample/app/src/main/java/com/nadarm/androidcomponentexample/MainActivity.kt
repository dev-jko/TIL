package com.nadarm.androidcomponentexample

import android.content.ComponentName
import android.content.Context
import android.content.Intent
import android.content.ServiceConnection
import android.os.Bundle
import android.os.IBinder
import androidx.appcompat.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {


    private var bound = false
    private lateinit var service: MyIntentService
    private val connection = object : ServiceConnection {
        override fun onServiceDisconnected(name: ComponentName?) {
            bound = false
        }

        override fun onServiceConnected(name: ComponentName?, service: IBinder?) {
            this@MainActivity.service = (service as MyIntentService.MyBinder).getService()
            bound = true
        }
    }

    init {
        println("main activity init")
    }

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
//            startService(intent)
            bindService(intent, this.connection, Context.BIND_AUTO_CREATE)
        }

        buttonEnd2.setOnClickListener {
            if (this.bound)
                this.service.makeToast()
        }


    }

    override fun onStop() {
        super.onStop()
        if (this.bound) {
            unbindService(this.connection)
            this.bound = false
        }
    }
}
