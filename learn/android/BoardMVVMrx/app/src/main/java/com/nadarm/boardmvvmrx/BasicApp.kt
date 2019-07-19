package com.nadarm.boardmvvmrx

import android.app.Application
import com.nadarm.boardmvvmrx.data.local.ArticleDatabase
import com.nadarm.boardmvvmrx.data.local.ArticleLocalDataSource
import com.nadarm.boardmvvmrx.data.remote.ArticleRemoteDataSource

class BasicApp : Application() {

    fun getRepository(): ArticleRepository {
        return ArticleRepository.getInstance(
            ArticleLocalDataSource.getInstance(ArticleDatabase.getInstance(this).articleDao()),
            ArticleRemoteDataSource
        )
    }
}