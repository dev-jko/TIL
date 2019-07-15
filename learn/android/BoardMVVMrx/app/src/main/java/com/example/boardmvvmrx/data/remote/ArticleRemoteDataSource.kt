package com.example.boardmvvmrx.data.remote

import com.example.boardmvvmrx.ArticleDataSource
import com.example.boardmvvmrx.data.Article
import io.reactivex.Completable
import io.reactivex.Flowable
import io.reactivex.Observable

object ArticleRemoteDataSource : ArticleDataSource {
    override fun getAllArticles(): Flowable<List<Article>> {
        // TODO
        return Flowable.empty()
    }

    override fun getArticle(articleId: Long): Observable<Article> {
        // TODO
        return Observable.empty()
    }

    override fun insertArticle(article: Article): Completable {
        // TODO
        return Completable.complete()
    }
}