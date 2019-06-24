package com.example.retrofitexample

import android.os.Bundle
import android.util.Log
import android.view.View
import androidx.appcompat.app.AppCompatActivity
import com.google.gson.JsonObject
import kotlinx.android.synthetic.main.activity_main.*
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }


    fun onSearch(view: View) {
        val string = et.text.toString()

        if (!string.isEmpty()) {
            val res = NetRetrofit.getInstance().service.getListRepos(string)
            res.enqueue(
                object : Callback<ArrayList<JsonObject>> {
                    override fun onFailure(call: Call<ArrayList<JsonObject>>, t: Throwable) {
                        Log.e("Err", t.message)
                    }

                    override fun onResponse(
                        call: Call<ArrayList<JsonObject>>,
                        response: Response<ArrayList<JsonObject>>
                    ) {
                        Log.d("Retrofit", response.toString())
                        if (response.body() != null) {
                            tv.text = response.body().toString()
                        }
                    }

                })
        }

    }


}
