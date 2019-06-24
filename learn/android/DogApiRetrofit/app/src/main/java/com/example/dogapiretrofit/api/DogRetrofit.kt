package com.example.dogapiretrofit.api

import com.google.gson.JsonObject
import io.reactivex.Observable
import retrofit2.Retrofit
import retrofit2.adapter.rxjava2.RxJava2CallAdapterFactory

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
        .addCallAdapterFactory(RxJava2CallAdapterFactory.create())
        .build()

    val service: DogAPI = retrofit.create(DogAPI::class.java)


    fun getDogImgUrlObservable(): Observable<JsonObject> {
        val res = DogRetrofit.getInstance().service.getRandomImgUrl()
        return res
    }

}