package com.example.helloworld

import android.content.Context
import android.os.AsyncTask
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.ProgressBar
import kotlinx.android.synthetic.main.activity_main3.*


class Main3Activity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main3)


        async_button.setOnClickListener {
            MyAsync(main3_progress).execute()
        }


    }


    class MyAsync(val progressBar: ProgressBar) : AsyncTask<Unit, Int, Unit>() {


        override fun doInBackground(vararg params: Unit?) {
            for (i in 0..100) {
                Thread.sleep(150)
                publishProgress(i)
            }
        }

        override fun onProgressUpdate(vararg values: Int?) {
            super.onProgressUpdate(*values)
            progressBar.progress = values[0]!!
        }

    }

}
