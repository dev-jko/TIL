package com.example.mvvm.model

import io.reactivex.Single

interface Repository {
    fun getShortenUrl(url:String): Single<ShortenUrl>
}