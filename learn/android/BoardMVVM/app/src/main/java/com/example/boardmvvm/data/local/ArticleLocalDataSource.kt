package com.example.boardmvvm.data.local

import com.example.boardmvvm.ArticleDataSource
import com.example.boardmvvm.data.Article
import io.reactivex.Completable
import io.reactivex.Flowable
import io.reactivex.Single

class ArticleLocalDataSource private constructor(
    val articleDao: ArticleDao
) : ArticleDataSource {

    override fun getAllArticles(): Flowable<List<Article>> {
        return articleDao.getAllArticles()
    }

    override fun getArticle(articleId: Long): Single<Article> {
        return articleDao.getArticle(articleId)
    }

    override fun insertArticle(article: Article): Completable {
        return articleDao.insertArticle(article)
    }

    companion object {
        private var INSTATNCE: ArticleLocalDataSource? = null

        fun getInstance(articleDao: ArticleDao): ArticleLocalDataSource {
            if (INSTATNCE == null) {
                synchronized(this) {
                    INSTATNCE = ArticleLocalDataSource(articleDao)
                }
            }
            return INSTATNCE!!
        }
    }
}