package com.example.boardmvvm.viewModel

import com.example.boardmvvm.ArticleRepository
import com.example.boardmvvm.data.Article
import io.reactivex.Observable
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.rxkotlin.addTo
import io.reactivex.schedulers.Schedulers
import java.util.concurrent.TimeUnit

class NewArticlePresenter(
    private val view: NewArticleContract.View,
    private val repository: ArticleRepository
) : NewArticleContract.Presenter {
    private val compositeDisposable = CompositeDisposable()

    override fun onDestroy() {
        compositeDisposable.dispose()
    }

    private fun insertArticle(article: Article) {
        repository.insertArticle(article)
            .subscribeOn(Schedulers.io())
            .observeOn(AndroidSchedulers.mainThread())
            .subscribe(
                { onInsertionCompleted() },
                { it.printStackTrace() }
            ).addTo(compositeDisposable)
    }

    private fun getNewArticle(): Article {
        return Article(
            view.getTitleText(),
            view.getContentText()
        )
    }

    private fun onInsertionCompleted() {
        view.makeToast("글이 작성됐습니다.")
        Observable.just(1)
            .subscribeOn(Schedulers.computation())
            .delay(1, TimeUnit.SECONDS)
            .observeOn(AndroidSchedulers.mainThread())
            .subscribe { view.finish() }
            .addTo(compositeDisposable)
    }

    override fun onSaveButtonClicked() {
        val newArticle = getNewArticle()
        insertArticle(newArticle)
    }

}