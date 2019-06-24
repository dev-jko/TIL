package com.example.retrofitexample

import com.google.gson.JsonObject
import retrofit2.Call
import retrofit2.http.GET
import retrofit2.http.Path

interface RetrofitService {
    @GET("users/{user}/repos")
    fun getListRepos(@Path("user") id: String): Call<ArrayList<JsonObject>>
}