package com.example.boardmvvmrx

import com.example.boardmvvmrx.data.Article
import io.reactivex.Flowable
import io.reactivex.Observable
import io.reactivex.Single
import io.reactivex.schedulers.Schedulers

class ArticleRepository private constructor(
    private val articleLocalDataSource: ArticleDataSource,
    private val articleRemoteDataSource: ArticleDataSource
) : ArticleDataSource {


    override fun getAllArticles(): Flowable<List<Article>> {
        return articleLocalDataSource.getAllArticles().subscribeOn(Schedulers.io())
//        articleRemoteDataSource.getAllArticles()
    }

    override fun getArticle(articleId: Long): Observable<Article> {
        // TODO add remote
        return articleLocalDataSource.getArticle(articleId).subscribeOn(Schedulers.io())
    }

    override fun insertArticle(article: Article): Single<Long> {
        // TODO add remote
        return articleLocalDataSource.insertArticle(article).subscribeOn(Schedulers.io())
    }

    override fun updateArticle(article: Article): Single<Int> {
        // TODO add remote
        return articleLocalDataSource.updateArticle(article).subscribeOn(Schedulers.io())
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