package com.example.boardmvvmrx

import com.example.boardmvvmrx.data.Article
import io.reactivex.Flowable
import io.reactivex.Observable

interface ArticleDataSource {

    fun getAllArticles(): Flowable<List<Article>>

    fun getArticle(articleId: Long): Observable<Article>

    fun insertArticle(article: Article)
}