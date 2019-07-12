package com.example.boardmvvm.viewModel

import android.app.Application
import android.content.Intent
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.LiveData
import androidx.lifecycle.LiveDataReactiveStreams
import androidx.lifecycle.MutableLiveData
import com.example.boardmvvm.ArticleRepository
import com.example.boardmvvm.BasicApp
import com.example.boardmvvm.data.Article
import io.reactivex.Observable
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.rxkotlin.addTo
import io.reactivex.schedulers.Schedulers
import io.reactivex.subjects.BehaviorSubject
import io.reactivex.subjects.PublishSubject

class DetailViewModel(application: Application) : AndroidViewModel(application) {
    private val repository: ArticleRepository by lazy { (application as BasicApp).getRepository() }
    private val compositeDisposable = CompositeDisposable()

    private val _article: MutableLiveData<Article> = MutableLiveData<Article>()
    val article: LiveData<Article> get() = _article

    private val intent: BehaviorSubject<Intent> = BehaviorSubject.create()

    fun initViewModel() {
        articleFromIntent()
            .subscribeOn(Schedulers.io())
            .subscribe { article -> _article.postValue(article) }
            .addTo(compositeDisposable)
    }

    private fun articleFromIntent(): Observable<Article> {
        return intent
            .map { it.getLongExtra("articleId", 1) }
            .map { articleId -> repository.getArticle(articleId).blockingGet() }
    }

    override fun onCleared() {
        compositeDisposable.dispose()
        super.onCleared()
    }

    fun intent(intent: Intent) {
        this.intent.onNext(intent)
    }
}