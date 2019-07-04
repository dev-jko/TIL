package com.example.boardmvc

import android.app.Application
import com.example.boardmvc.model.Article
import com.example.boardmvc.model.ArticleDao
import com.example.boardmvc.model.ArticleDatabase
import io.reactivex.Completable
import io.reactivex.Flowable
import io.reactivex.Single

class ArticleRepository(application: Application) {

    private val articleDao: ArticleDao by lazy {
        ArticleDatabase.getInstance(application).articleDao()
    }

    fun getAllArticles(): Flowable<List<Article>> {
        return articleDao.getAllArticles()
    }

    fun getArticle(articleId: Long): Single<Article> {
        return articleDao.getArticle(articleId)
    }

    fun insertArticle(article: Article): Completable {
        return articleDao.insertArticle(article)
    }


}