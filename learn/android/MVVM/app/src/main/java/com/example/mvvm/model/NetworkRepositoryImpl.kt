package com.example.mvvm.model

import io.reactivex.Single

class NetworkRepositoryImpl(private val api: Api) : Repository {
    override fun getShortenUrl(url: String): Single<ShortenUrl> {
        return api.shortUrl(url)
            .map { it.result }
    }
}