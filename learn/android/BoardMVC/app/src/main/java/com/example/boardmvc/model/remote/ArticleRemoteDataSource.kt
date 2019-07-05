package com.example.boardmvc.model.remote

import com.example.boardmvc.ArticleDataSource
import com.example.boardmvc.model.Article
import io.reactivex.Completable
import io.reactivex.Flowable
import io.reactivex.Single

object ArticleRemoteDataSource : ArticleDataSource {
    override fun getAllArticles(): Flowable<List<Article>> {
        // TODO
        return Flowable.empty()
    }

    override fun getArticle(articleId: Long): Single<Article> {
        // TODO
        return Single.never()
    }

    override fun insertArticle(article: Article): Completable {
        // TODO
        return Completable.never()
    }
}