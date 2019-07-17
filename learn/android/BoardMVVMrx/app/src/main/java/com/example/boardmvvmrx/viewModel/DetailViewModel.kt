package com.example.boardmvvmrx.viewModel

import android.app.Application
import android.content.Intent
import androidx.lifecycle.AndroidViewModel
import com.example.boardmvvmrx.ArticleRepository
import com.example.boardmvvmrx.BasicApp
import com.example.boardmvvmrx.data.Article
import io.reactivex.Observable
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.functions.BiFunction
import io.reactivex.schedulers.Schedulers
import io.reactivex.subjects.BehaviorSubject
import io.reactivex.subjects.PublishSubject


interface DetailViewModel {

    interface Inputs {
        fun intent(intent: Intent)
        fun editClicked()
    }

    interface Outputs {
        fun article(): Observable<Article>
        fun startEditActivity(): Observable<Long>
    }

    class ViewModel(application: Application) : AndroidViewModel(application), Inputs, Outputs {
        private val repository: ArticleRepository by lazy { (application as BasicApp).getRepository() }

        private val intent: PublishSubject<Intent> = PublishSubject.create()
        private val editClicked: PublishSubject<Unit> = PublishSubject.create()

        private val article: BehaviorSubject<Article> = BehaviorSubject.create()
        private val startEditActivity: BehaviorSubject<Long> = BehaviorSubject.create()

        val inputs: Inputs = this
        val outputs: Outputs = this

        init {
            val articleIdObservable = this.intent
                .map { intent -> intent.getLongExtra("articleId", 1) }
                .subscribeOn(Schedulers.io())

            articleIdObservable
                .flatMap(repository::getArticle)
                .subscribe(this.article)

            this.editClicked
                .withLatestFrom(articleIdObservable, BiFunction<Unit, Long, Long> { _, articleId -> articleId })
                .subscribe(this.startEditActivity)

        }

        override fun article(): Observable<Article> = this.article
        override fun startEditActivity(): Observable<Long> = this.startEditActivity

        override fun intent(intent: Intent) {
            this.intent.onNext(intent)
        }

        override fun editClicked() {
            this.editClicked.onNext(Unit)
        }
    }
}