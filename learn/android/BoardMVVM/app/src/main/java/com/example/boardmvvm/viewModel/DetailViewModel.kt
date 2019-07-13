package com.example.boardmvvm.viewModel

import android.app.Application
import android.content.Intent
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.Transformations
import com.example.boardmvvm.ArticleRepository
import com.example.boardmvvm.BasicApp
import com.example.boardmvvm.data.Article
import io.reactivex.disposables.CompositeDisposable

class DetailViewModel(application: Application) : AndroidViewModel(application) {
    private val repository: ArticleRepository by lazy { (application as BasicApp).getRepository() }
    private val compositeDisposable = CompositeDisposable()

    private val intent: MutableLiveData<Intent> = MutableLiveData<Intent>()
    private val article: LiveData<Article> =
        Transformations.switchMap(articleIdFromIntent()) { articleId -> repository.getArticle(articleId) }


    private fun articleIdFromIntent(): LiveData<Long> =
        Transformations.map(intent) { intent -> intent.getLongExtra("articleId", 1) }

    override fun onCleared() {
        compositeDisposable.dispose()
        super.onCleared()
    }

    fun intent(intent: Intent) = this.intent.postValue(intent)
    fun article(): LiveData<Article> = this.article
}