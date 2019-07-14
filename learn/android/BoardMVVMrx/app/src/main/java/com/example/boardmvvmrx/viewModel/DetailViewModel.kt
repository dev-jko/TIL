package com.example.boardmvvmrx.viewModel

import android.app.Application
import android.content.Intent
import androidx.lifecycle.AndroidViewModel
import com.example.boardmvvmrx.ArticleRepository
import com.example.boardmvvmrx.BasicApp
import com.example.boardmvvmrx.data.Article
import io.reactivex.Observable
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.schedulers.Schedulers
import io.reactivex.subjects.BehaviorSubject
import io.reactivex.subjects.PublishSubject


interface DetailViewModel {

    interface Inputs {
        fun intent(intent: Intent)
    }

    interface Outputs {
        fun article(): Observable<Article>
    }

    class ViewModel(application: Application) : AndroidViewModel(application), Inputs, Outputs {
        private val repository: ArticleRepository by lazy { (application as BasicApp).getRepository() }
        private val compositeDisposable: CompositeDisposable = CompositeDisposable()

        private val intent: PublishSubject<Intent> = PublishSubject.create()
        private val article: BehaviorSubject<Article> = BehaviorSubject.create()

        val inputs: Inputs = this
        val outputs: Outputs = this

        init {
            this.intent()
                .map { intent -> intent.getLongExtra("articleId", 1) }
                .flatMap(repository::getArticle)
                .subscribeOn(Schedulers.io())
                .subscribe { article -> this.article.onNext(article) }
                .apply { compositeDisposable }
        }

        override fun article(): Observable<Article> = this.article

        override fun intent(intent: Intent) {
            this.intent.onNext(intent)
        }

        private fun intent(): Observable<Intent> = this.intent

        override fun onCleared() {
            compositeDisposable.dispose()
            super.onCleared()
        }

    }
}
