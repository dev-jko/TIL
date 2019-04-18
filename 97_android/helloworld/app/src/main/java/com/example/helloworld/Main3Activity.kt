package com.example.helloworld

import android.os.AsyncTask
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.os.Parcel
import android.os.Parcelable
import kotlinx.android.synthetic.main.activity_main3.*

class Main3Activity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main3)

        async_button.setOnClickListener {

        }


    }


    class MyAsync : AsyncTask<Int, Int, Int>() {

        override fun onPostExecute(result: Int?) {
            super.onPostExecute(result)
        }

        override fun doInBackground(vararg params: Int?): Int {
            publishProgress()
        }

        override fun onProgressUpdate(vararg values: Int?) {
            super.onProgressUpdate(*values)
        }

    }

}
