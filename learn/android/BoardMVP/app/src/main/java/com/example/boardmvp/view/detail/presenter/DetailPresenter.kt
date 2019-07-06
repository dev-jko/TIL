package com.example.boardmvp.view.detail.presenter

import com.example.boardmvp.ArticleRepository
import com.example.boardmvp.data.local.ArticleDatabase
import com.example.boardmvp.data.local.ArticleLocalDataSource
import com.example.boardmvp.data.remote.ArticleRemoteDataSource
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.rxkotlin.addTo
import io.reactivex.schedulers.Schedulers

class DetailPresenter(private val view: DetailContract.View) : DetailContract.Presenter {

    private val compositeDisposable = CompositeDisposable()
    private val repository: ArticleRepository by lazy {
        ArticleRepository.getInstance(
            ArticleLocalDataSource.getInstance(ArticleDatabase.getInstance(application).articleDao()),
            ArticleRemoteDataSource
        )
    }

    override fun onCreate() {
        val articleId = view.getArticleIdFromIntent()
        loadArticle(articleId)
    }

    override fun onDestroy() {
        compositeDisposable.dispose()
    }

    private fun loadArticle(articleId: Long) {
        repository.getArticle(articleId)
            .subscribeOn(Schedulers.io())
            .observeOn(AndroidSchedulers.mainThread())
            .subscribe(
                {
                    view.showArticle(it.title, it.content)
                },
                { it.printStackTrace() }
            ).addTo(compositeDisposable)
    }
}