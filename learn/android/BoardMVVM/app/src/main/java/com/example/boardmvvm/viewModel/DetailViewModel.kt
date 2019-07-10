package com.example.boardmvvm.viewModel

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import com.example.boardmvvm.ArticleRepository
import com.example.boardmvvm.BasicApp
import com.example.boardmvvm.data.Article
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.rxkotlin.addTo
import io.reactivex.schedulers.Schedulers

class DetailViewModel(application: Application) : AndroidViewModel(application) {
    private val repository: ArticleRepository by lazy { (application as BasicApp).getRepository() }
    private val compositeDisposable = CompositeDisposable()

    private val _article: MutableLiveData<Article> = MutableLiveData<Article>()
    val article: LiveData<Article> get() = _article

    override fun onCleared() {
        compositeDisposable.dispose()
        super.onCleared()
    }

    fun loadArticle(articleId: Long) {
        repository.getArticle(articleId)
            .subscribeOn(Schedulers.io())
//            .observeOn(AndroidSchedulers.mainThread())
            .subscribe(
                { _article.postValue(it) },
                { it.printStackTrace() }
            ).addTo(compositeDisposable)
    }
}