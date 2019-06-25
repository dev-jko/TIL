package com.example.dogapiretrofit.api

import io.reactivex.Observable
import retrofit2.Retrofit
import retrofit2.adapter.rxjava2.RxJava2CallAdapterFactory
import retrofit2.converter.gson.GsonConverterFactory

class DogRetrofit {

    companion object {

        private val baseUrl = "https://dog.ceo/api/"
        private var INSTANCE: DogRetrofit? = null

        fun getInstance(): DogRetrofit {
            if (INSTANCE == null) {
                synchronized(DogRetrofit::class) {
                    INSTANCE = DogRetrofit()
                }
            }
            return INSTANCE as DogRetrofit
        }
    }

    val retrofit: Retrofit = Retrofit.Builder()
        .baseUrl(baseUrl)
        .addConverterFactory(GsonConverterFactory.create())
        .addCallAdapterFactory(RxJava2CallAdapterFactory.create())
        .build()

    val service: DogAPI = retrofit.create(DogAPI::class.java)


    fun getDogImgUrlObservable(): Observable<String> {
        return DogRetrofit.getInstance().service.getRandomImgUrl()
            .filter { it.status == "success" }
            .map { it.message }
    }

}