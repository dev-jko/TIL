package com.example.boardmvvm.viewModel

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import com.example.boardmvvm.ArticleRepository
import com.example.boardmvvm.BasicApp
import com.example.boardmvvm.data.Article
import com.example.boardmvvm.view.adapter.ArticleAdapter
import io.reactivex.disposables.CompositeDisposable

interface ListViewModel {
    interface Inputs : ArticleAdapter.Delegate {
        fun newArticleClicked()
    }

    interface Outputs {
        fun articles(): LiveData<List<Article>>
        fun startDetailActivity(): LiveData<Article>
        fun startNewArticleActivity(): LiveData<Boolean>
    }

    class ViewModel(application: Application) : AndroidViewModel(application),
        ListViewModel.Inputs, ListViewModel.Outputs {

        private val repository: ArticleRepository by lazy { (application as BasicApp).getRepository() }
        private val compositeDisposable = CompositeDisposable()

        private val articleClicked: MutableLiveData<Article> = MutableLiveData()

        private val articles: LiveData<List<Article>> = repository.getAllArticles()
        private val startDetailActivity: LiveData<Article> = articleClicked
        private val startNewArticleActivity: MutableLiveData<Boolean> = MutableLiveData()

        val inputs: Inputs = this
        val outputs: Outputs = this

        override fun articles(): LiveData<List<Article>> = this.articles
        override fun startDetailActivity(): LiveData<Article> = this.startDetailActivity
        override fun startNewArticleActivity(): LiveData<Boolean> = this.startNewArticleActivity

        override fun newArticleClicked() {
            this.startNewArticleActivity.postValue(true)
        }

        override fun articleClicked(article: Article) {
            this.articleClicked.postValue(article)
        }

        override fun onCleared() {
            compositeDisposable.dispose()
            super.onCleared()
        }

    }
}