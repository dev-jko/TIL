package com.example.dogapiretrofit.vo

import com.google.gson.annotations.Expose
import com.google.gson.annotations.SerializedName

data class DogResponse(

    @SerializedName("message")
    @Expose
    val message: String,

    @SerializedName("status")
    @Expose
    val status: String
)