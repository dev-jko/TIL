package com.example.boardmvp

import android.app.Application
import com.example.boardmvp.data.local.ArticleDatabase
import com.example.boardmvp.data.local.ArticleLocalDataSource
import com.example.boardmvp.data.remote.ArticleRemoteDataSource

class BasicApp : Application() {

    fun getRepository(): ArticleRepository {
        return ArticleRepository.getInstance(
            ArticleLocalDataSource.getInstance(ArticleDatabase.getInstance(this).articleDao()),
            ArticleRemoteDataSource
        )
    }
}