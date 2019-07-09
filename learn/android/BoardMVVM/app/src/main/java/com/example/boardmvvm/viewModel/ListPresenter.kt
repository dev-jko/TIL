package com.example.boardmvvm.viewModel

import com.example.boardmvvm.ArticleRepository
import com.example.boardmvvm.view.adapter.ArticleAdapterContract
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.rxkotlin.addTo
import io.reactivex.schedulers.Schedulers

class ListPresenter(
    private val view: ListContract.View,
    private val adapterModel: ArticleAdapterContract.Model,
    private val repository: ArticleRepository
) : ListContract.Presenter {
    private val compositeDisposable = CompositeDisposable()

    override fun onCreate() {
        repository.getAllArticles()
            .subscribeOn(Schedulers.io())
            .observeOn(AndroidSchedulers.mainThread())
            .subscribe {
                adapterModel.changeList(it)
                view.refresh()
            }
            .addTo(compositeDisposable)
    }

    override fun onDestroy() {
        compositeDisposable.dispose()
    }

    override fun onAddButtonClick() {
        view.startNewArticleActivity()
    }
}