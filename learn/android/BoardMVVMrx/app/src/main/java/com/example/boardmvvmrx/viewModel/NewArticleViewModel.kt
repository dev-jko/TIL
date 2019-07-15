package com.example.boardmvvmrx.viewModel

import android.app.Application
import android.widget.Toast
import androidx.lifecycle.AndroidViewModel
import com.example.boardmvvmrx.ArticleRepository
import com.example.boardmvvmrx.BasicApp
import com.example.boardmvvmrx.data.Article
import io.reactivex.Observable
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.functions.Function3
import io.reactivex.rxkotlin.addTo
import io.reactivex.schedulers.Schedulers
import io.reactivex.subjects.BehaviorSubject
import io.reactivex.subjects.PublishSubject
import java.util.concurrent.TimeUnit

interface NewArticleViewModel {

    interface Inputs {
        fun titleChanged(title: String)
        fun contentChanged(content: String)
        fun saveClicked()
    }

    interface Outputs {
        fun finishActivity(): Observable<Boolean>
        fun makeToast(): Observable<Pair<String, Int>>
    }

    class ViewModel(application: Application) : AndroidViewModel(application), Inputs, Outputs {
        private val repository: ArticleRepository by lazy { (application as BasicApp).getRepository() }
        private val compositeDisposable = CompositeDisposable()

        private val titleChanged: PublishSubject<String> = PublishSubject.create()
        private val contentChanged: PublishSubject<String> = PublishSubject.create()
        private val saveClicked: PublishSubject<Boolean> = PublishSubject.create()

        private val finishActivity: BehaviorSubject<Boolean> = BehaviorSubject.create()
        private val makeToast: BehaviorSubject<Pair<String, Int>> = BehaviorSubject.create()

        val inputs: Inputs = this
        val outputs: Outputs = this

        init {
            this.saveClicked
                .throttleFirst(500, TimeUnit.MILLISECONDS)
                .withLatestFrom<String, String, Article>(
                    this.titleChanged,
                    this.contentChanged,
                    Function3 { _, title, content -> Article(title, content) }
                )
                .subscribeOn(Schedulers.io())
                .subscribe { article -> insertArticle(article) }
                .addTo(compositeDisposable)
        }

        override fun finishActivity(): Observable<Boolean> = finishActivity
        override fun makeToast(): Observable<Pair<String, Int>> = makeToast

        override fun onCleared() {
            compositeDisposable.dispose()
            super.onCleared()
        }

        override fun titleChanged(title: String) {
            this.titleChanged.onNext(title)
        }

        override fun contentChanged(content: String) {
            this.contentChanged.onNext(content)
        }

        override fun saveClicked() {
            this.saveClicked.onNext(true)
        }

        private fun insertArticle(article: Article) {
            repository.insertArticle(article)
                .subscribeOn(Schedulers.io())
                .subscribe(
                    { onInsertionCompleted() },
                    { onInsertionError() }
                )
                .addTo(compositeDisposable)
        }

        private fun onInsertionError() {
            this.makeToast.onNext("작성 실패" to Toast.LENGTH_SHORT)
        }

        private fun onInsertionCompleted() {
            this.makeToast.onNext("글이 작성됐습니다." to Toast.LENGTH_SHORT)
            Observable.timer(600, TimeUnit.MILLISECONDS)
                .subscribeOn(Schedulers.computation())
                .subscribe { this.finishActivity.onNext(true) }
                .addTo(compositeDisposable)
        }

    }

}
