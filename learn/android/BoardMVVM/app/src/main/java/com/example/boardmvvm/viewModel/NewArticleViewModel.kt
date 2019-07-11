package com.example.boardmvvm.viewModel

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import com.example.boardmvvm.ArticleRepository
import com.example.boardmvvm.BasicApp
import com.example.boardmvvm.data.Article
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.rxkotlin.addTo
import io.reactivex.schedulers.Schedulers

class NewArticleViewModel(application: Application) : AndroidViewModel(application) {
    private val repository: ArticleRepository by lazy { (application as BasicApp).getRepository() }
    private val compositeDisposable = CompositeDisposable()

    val title: MutableLiveData<String> = MutableLiveData()
    val content: MutableLiveData<String> = MutableLiveData()

    fun onDestroy() {
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
        return Article(title.value!!, content.value!!)
    }

    private fun onInsertionCompleted() {
//        view.makeToast("글이 작성됐습니다.")
//        Observable.just(1)
//            .subscribeOn(Schedulers.computation())
//            .delay(1, TimeUnit.SECONDS)
//            .observeOn(AndroidSchedulers.mainThread())
//            .subscribe { view.finish() }
//            .addTo(compositeDisposable)
    }

    fun onSaveButtonClicked() {
        val newArticle = getNewArticle()
        insertArticle(newArticle)
    }

}