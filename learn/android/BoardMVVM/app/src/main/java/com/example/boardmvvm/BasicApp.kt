package com.example.boardmvvm

import android.app.Application
import com.example.boardmvvm.data.local.ArticleDatabase
import com.example.boardmvvm.data.local.ArticleLocalDataSource
import com.example.boardmvvm.data.remote.ArticleRemoteDataSource

class BasicApp : Application() {

    fun getRepository(): ArticleRepository {
        return ArticleRepository.getInstance(
            ArticleLocalDataSource.getInstance(ArticleDatabase.getInstance(this).articleDao()),
            ArticleRemoteDataSource
        )
    }
}