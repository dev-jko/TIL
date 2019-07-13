package com.example.boardmvvm

import androidx.lifecycle.LiveData
import androidx.lifecycle.MediatorLiveData
import androidx.lifecycle.Observer
import androidx.lifecycle.Transformations
import com.example.boardmvvm.data.Article
import io.reactivex.Completable
import io.reactivex.Flowable
import io.reactivex.Single

class ArticleRepository private constructor(
    private val articleLocalDataSource: ArticleDataSource,
    private val articleRemoteDataSource: ArticleDataSource
) : ArticleDataSource {


    override fun getAllArticles(): LiveData<List<Article>> {
        return articleLocalDataSource.getAllArticles()
//        articleRemoteDataSource.getAllArticles()
    }

    override fun getArticle(articleId: Long): LiveData<Article> {
        // TODO add remote
        return articleLocalDataSource.getArticle(articleId)
    }

    override fun insertArticle(article: Article) {
        // TODO add remote
        articleLocalDataSource.insertArticle(article)
    }


    companion object {
        private var INSTANCE: ArticleRepository? = null

        fun getInstance(
            articleLocalDataSource: ArticleDataSource,
            articleRemoteDataSource: ArticleDataSource
        ): ArticleRepository {
            if (INSTANCE == null) {
                synchronized(this) {
                    INSTANCE = ArticleRepository(articleLocalDataSource, articleRemoteDataSource)
                }
            }
            return INSTANCE!!
        }
    }

}