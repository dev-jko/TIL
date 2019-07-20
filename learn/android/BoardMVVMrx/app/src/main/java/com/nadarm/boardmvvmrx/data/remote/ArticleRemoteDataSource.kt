package com.nadarm.boardmvvmrx.data.remote

import com.nadarm.boardmvvmrx.domain.repository.ArticleRepository
import com.nadarm.boardmvvmrx.data.Article
import io.reactivex.Flowable
import io.reactivex.Observable
import io.reactivex.Single

object ArticleRemoteDataSource : ArticleRepository {
    override fun getAllArticles(): Flowable<List<Article>> {
        // TODO
        return Flowable.empty()
    }

    override fun getArticle(articleId: Long): Flowable<com.nadarm.boardmvvmrx.domain.entity.Article> {
        // TODO
        return Observable.empty()
    }

    override fun insertArticle(article: Article): Single<Long> {
        // TODO
        return Single.create { 1 }
    }

    override fun updateArticle(article: Article): Single<Int> {
        // TODO
        return Single.create { 1 }
    }

    override fun deleteArticle(article: Article): Single<Int> {
        // TODO
        return Single.create { 1 }
    }
}