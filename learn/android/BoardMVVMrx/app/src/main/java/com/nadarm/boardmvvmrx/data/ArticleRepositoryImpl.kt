package com.nadarm.boardmvvmrx.data

import com.nadarm.boardmvvmrx.domain.repository.ArticleRepository
import io.reactivex.Flowable
import io.reactivex.Single
import io.reactivex.schedulers.Schedulers

class ArticleRepositoryImpl private constructor(
    private val articleLocalDataSource: ArticleRepository,
    private val articleRemoteDataSource: ArticleRepository
) : ArticleRepository {


    override fun getAllArticles(): Flowable<List<Article>> {
        return articleLocalDataSource.getAllArticles().subscribeOn(Schedulers.io()).map { dataArticle -> com.nadarm.boardmvvmrx.domain.entity.Article(dataArticle) }
//        articleRemoteDataSource.getAllArticles()
    }

    override fun getArticle(articleId: Long): Flowable<com.nadarm.boardmvvmrx.domain.entity.Article> {
        // TODO add remote
        return articleLocalDataSource.getArticle(articleId).subscribeOn(Schedulers.io())
    }

    override fun insertArticle(article: Article): Single<Long> {
        // TODO add remote
        return articleLocalDataSource.insertArticle(article).subscribeOn(Schedulers.io())
    }

    override fun updateArticle(article: Article): Single<Int> {
        // TODO add remote
        return articleLocalDataSource.updateArticle(article).subscribeOn(Schedulers.io())
    }

    override fun deleteArticle(article: Article): Single<Int> {
        // TODO add remote
        return articleLocalDataSource.deleteArticle(article).subscribeOn(Schedulers.io())
    }

    companion object {
        private var INSTANCE: ArticleRepositoryImpl? = null

        fun getInstance(
            articleLocalDataSource: ArticleRepository,
            articleRemoteDataSource: ArticleRepository
        ): ArticleRepositoryImpl {
            if (INSTANCE == null) {
                synchronized(this) {
                    INSTANCE =
                        ArticleRepositoryImpl(
                            articleLocalDataSource,
                            articleRemoteDataSource
                        )
                }
            }
            return INSTANCE!!
        }
    }

}