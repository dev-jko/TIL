package com.example.boardmvp.data.remote

import com.example.boardmvp.ArticleDataSource
import com.example.boardmvp.data.Article
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