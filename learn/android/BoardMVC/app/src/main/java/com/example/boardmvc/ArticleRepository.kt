package com.example.boardmvc

import com.example.boardmvc.model.Article
import io.reactivex.Completable
import io.reactivex.Flowable
import io.reactivex.Single

class ArticleRepository private constructor(
    private val articleLocalDataSource: ArticleDataSource,
    private val articleRemoteDataSource: ArticleDataSource
) : ArticleDataSource {


    override fun getAllArticles(): Flowable<List<Article>> {
        return Flowable.concatArray(
            articleLocalDataSource.getAllArticles(),
            articleRemoteDataSource.getAllArticles()
        )

    }

    override fun getArticle(articleId: Long): Single<Article> {
        // TODO add remote
        return articleLocalDataSource.getArticle(articleId)
    }

    override fun insertArticle(article: Article): Completable {
        // TODO add remote
        return articleLocalDataSource.insertArticle(article)
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