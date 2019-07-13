package com.example.boardmvvm.viewModel

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import com.example.boardmvvm.ArticleRepository
import com.example.boardmvvm.BasicApp
import com.example.boardmvvm.data.Article
import io.reactivex.disposables.CompositeDisposable

class ListViewModel(application: Application) : AndroidViewModel(application) {
    private val repository: ArticleRepository by lazy { (application as BasicApp).getRepository() }
    private val compositeDisposable = CompositeDisposable()

    val articles: LiveData<List<Article>> = repository.getAllArticles()
    private val startNewArticleActivity: MutableLiveData<Boolean> = MutableLiveData()

    fun startNewArticleActivity():LiveData<Boolean> = this.startNewArticleActivity

    override fun onCleared() {
        compositeDisposable.dispose()
        super.onCleared()
    }

    fun onNewArticleClicked() {
        startNewArticleActivity.postValue(true)
    }

}