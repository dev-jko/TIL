package com.example.boardmvvmrx

import android.app.Application
import com.example.boardmvvmrx.data.local.ArticleDatabase
import com.example.boardmvvmrx.data.local.ArticleLocalDataSource
import com.example.boardmvvmrx.data.remote.ArticleRemoteDataSource

class BasicApp : Application() {

    fun getRepository(): ArticleRepository {
        return ArticleRepository.getInstance(
            ArticleLocalDataSource.getInstance(ArticleDatabase.getInstance(this).articleDao()),
            ArticleRemoteDataSource
        )
    }
}