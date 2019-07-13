package com.example.boardmvvm.data.local

import androidx.lifecycle.LiveData
import com.example.boardmvvm.ArticleDataSource
import com.example.boardmvvm.data.Article
import io.reactivex.Completable
import io.reactivex.Flowable
import io.reactivex.Single

class ArticleLocalDataSource private constructor(
    val articleDao: ArticleDao
) : ArticleDataSource {

    override fun getAllArticles(): LiveData<List<Article>> {
        return articleDao.getAllArticles()
    }

    override fun getArticle(articleId: Long): LiveData<Article> {
        return articleDao.getArticle(articleId)
    }

    override fun insertArticle(article: Article) {
        articleDao.insertArticle(article)
    }

    companion object {
        private var INSTANCE: ArticleLocalDataSource? = null

        fun getInstance(articleDao: ArticleDao): ArticleLocalDataSource {
            if (INSTANCE == null) {
                synchronized(this) {
                    INSTANCE = ArticleLocalDataSource(articleDao)
                }
            }
            return INSTANCE!!
        }
    }
}