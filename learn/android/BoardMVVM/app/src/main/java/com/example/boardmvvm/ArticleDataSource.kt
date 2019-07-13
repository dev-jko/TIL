package com.example.boardmvvm

import androidx.lifecycle.LiveData
import com.example.boardmvvm.data.Article
import io.reactivex.Completable
import io.reactivex.Flowable
import io.reactivex.Single

interface ArticleDataSource {

    fun getAllArticles(): LiveData<List<Article>>

    fun getArticle(articleId: Long): LiveData<Article>

    fun insertArticle(article: Article)
}