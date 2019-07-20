package com.nadarm.boardmvvmrx.presentation.viewModel

import android.app.Application
import android.widget.Toast
import androidx.lifecycle.AndroidViewModel
import com.nadarm.boardmvvmrx.data.ArticleRepositoryImpl
import com.nadarm.boardmvvmrx.BasicApp
import com.nadarm.boardmvvmrx.domain.entity.Article
import io.reactivex.Observable
import io.reactivex.functions.BiFunction
import io.reactivex.schedulers.Schedulers
import io.reactivex.subjects.BehaviorSubject
import io.reactivex.subjects.PublishSubject
import java.util.concurrent.TimeUnit

interface DeleteViewModel {

    interface Inputs {
        fun article(article: Article)
        fun deleteClicked()
    }

    interface Outputs {
        fun finishActivity(): Observable<Unit>
        fun makeToast(): Observable<Pair<String, Int>>
    }

    class ViewModel(application: Application) : AndroidViewModel(application), Inputs, Outputs {
        private val repository: ArticleRepositoryImpl by lazy { (application as BasicApp).getRepository() }

        private val article: PublishSubject<Article> = PublishSubject.create()
        private val deleteClicked: PublishSubject<Unit> = PublishSubject.create()

        private val finishActivity: BehaviorSubject<Unit> = BehaviorSubject.create()
        private val makeToast: BehaviorSubject<Pair<String, Int>> = BehaviorSubject.create()

        val inputs: Inputs = this
        val outputs: Outputs = this

        init {

            val deleteResult = this.deleteClicked
                .throttleFirst(500, TimeUnit.MILLISECONDS)
                .withLatestFrom(this.article, BiFunction<Unit, Article, Article> { _, article -> article })
                .flatMapSingle(repository::deleteArticle)
                .subscribeOn(Schedulers.io())
                .share()

            deleteResult
                .map { "삭제 완료" to Toast.LENGTH_SHORT }
                .doOnError { this.makeToast.onNext("삭제 실패" to Toast.LENGTH_SHORT) }
                .subscribe(this.makeToast)

            deleteResult
                .map { Unit }
                .delay(600, TimeUnit.MILLISECONDS)
                .subscribe(this.finishActivity)

        }

        override fun finishActivity(): Observable<Unit> = this.finishActivity
        override fun makeToast(): Observable<Pair<String, Int>> = this.makeToast

        override fun article(article: Article) {
            this.article.onNext(article)
        }

        override fun deleteClicked() {
            this.deleteClicked.onNext(Unit)
        }
    }


}