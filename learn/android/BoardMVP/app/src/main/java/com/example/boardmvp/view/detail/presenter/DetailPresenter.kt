package com.example.boardmvp.view.detail.presenter

import com.example.boardmvp.ArticleRepository
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.rxkotlin.addTo
import io.reactivex.schedulers.Schedulers

class DetailPresenter(
    private val view: DetailContract.View,
    private val repository: ArticleRepository
) : DetailContract.Presenter {

    private val compositeDisposable = CompositeDisposable()

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