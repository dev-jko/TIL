package com.example.boardmvvm.viewModel

import com.example.boardmvvm.ArticleRepository
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.rxkotlin.addTo
import io.reactivex.schedulers.Schedulers

class DetailPresenter(
    private val repository: ArticleRepository
) {

    private val compositeDisposable = CompositeDisposable()

    fun onCreate() {
        val articleId = view.getArticleIdFromIntent()
        loadArticle(articleId)
    }

    fun onDestroy() {
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