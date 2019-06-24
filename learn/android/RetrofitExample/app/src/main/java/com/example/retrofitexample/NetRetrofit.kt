package com.example.retrofitexample

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class NetRetrofit {

    companion object {
        private var ourInstance: NetRetrofit? = null

        fun getInstance(): NetRetrofit {
            if (ourInstance == null) {
                synchronized(NetRetrofit::class) {
                    ourInstance = NetRetrofit()
                }
            }
            return ourInstance as NetRetrofit
        }

    }

    val retrofit: Retrofit = Retrofit.Builder()
        .baseUrl("https://api.github.com/")
        .addConverterFactory(GsonConverterFactory.create())
        .build()

    val service: RetrofitService = retrofit.create(RetrofitService::class.java)


}