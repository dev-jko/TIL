package com.example.boardmvvmrx

import com.example.boardmvvmrx.data.Article
import io.reactivex.Flowable
import io.reactivex.Observable

class ArticleRepository private constructor(
    private val articleLocalDataSource: ArticleDataSource,
    private val articleRemoteDataSource: ArticleDataSource
) : ArticleDataSource {


    override fun getAllArticles(): Flowable<List<Article>> {
        return articleLocalDataSource.getAllArticles()
//        articleRemoteDataSource.getAllArticles()
    }

    override fun getArticle(articleId: Long): Observable<Article> {
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