package com.example.boardmvp.view.list.presenter

import com.example.boardmvp.ArticleRepository
import io.reactivex.disposables.CompositeDisposable

class ListPresenter(
    private val view: ListContract.View,
    private val repository: ArticleRepository
) : ListContract.Presenter {
    private val compositeDisposable = CompositeDisposable()


    override fun onDestroy() {
        compositeDisposable.dispose()
    }
}