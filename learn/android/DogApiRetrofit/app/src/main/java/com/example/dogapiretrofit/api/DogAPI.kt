package com.example.dogapiretrofit.api

import com.google.gson.JsonObject
import io.reactivex.Observable
import retrofit2.Call
import retrofit2.http.GET

interface DogAPI {

//    @GET("breeds/image/random")
//    fun getRandomImgUrl(): Call<JsonObject>

    @GET("breeds/image/random")
    fun getRandomImgUrl(): Observable<JsonObject>

}
