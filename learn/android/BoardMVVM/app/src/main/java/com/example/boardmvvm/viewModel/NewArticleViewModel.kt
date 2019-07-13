package com.example.boardmvvm.viewModel

import android.app.Application
import android.widget.Toast
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import com.example.boardmvvm.ArticleRepository
import com.example.boardmvvm.BasicApp
import com.example.boardmvvm.data.Article
import io.reactivex.Observable
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.rxkotlin.addTo
import io.reactivex.schedulers.Schedulers
import java.util.concurrent.TimeUnit

class NewArticleViewModel(application: Application) : AndroidViewModel(application) {
    private val repository: ArticleRepository by lazy { (application as BasicApp).getRepository() }
    private val compositeDisposable = CompositeDisposable()

    val title: MutableLiveData<String> = MutableLiveData()
    val content: MutableLiveData<String> = MutableLiveData()
    private val finishActivity: MutableLiveData<Boolean> = MutableLiveData()
    private val makeToast: MutableLiveData<Pair<String, Int>> = MutableLiveData()

    fun finishActivity(): LiveData<Boolean> = finishActivity
    fun makeToast(): LiveData<Pair<String, Int>> = makeToast

    override fun onCleared() {
        compositeDisposable.dispose()
        super.onCleared()
    }

    fun onSaveButtonClicked() {
        val newArticle = getNewArticle()
        insertArticle(newArticle)
    }

    private fun getNewArticle(): Article {
        return Article(title.value!!, content.value!!)
    }

    private fun insertArticle(article: Article) {
        Observable.fromCallable { repository.insertArticle(article) }
            .subscribeOn(Schedulers.io())
            .subscribe { onInsertionCompleted() }
            .addTo(compositeDisposable)
    }

    private fun onInsertionCompleted() {
        makeToast.postValue("글이 작성됐습니다." to Toast.LENGTH_SHORT)
        Observable.just(1)
            .subscribeOn(Schedulers.computation())
            .delay(500, TimeUnit.MILLISECONDS)
            .subscribe { finishActivity.postValue(true) }
            .addTo(compositeDisposable)
    }


}