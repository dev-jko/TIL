package com.example.boardmvvmrx.viewModel

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import com.example.boardmvvmrx.ArticleRepository
import com.example.boardmvvmrx.BasicApp
import com.example.boardmvvmrx.data.Article
import io.reactivex.Observable
import io.reactivex.subjects.BehaviorSubject
import io.reactivex.subjects.PublishSubject

interface DeleteViewModel {

    interface Inputs {
        fun article(article: Article)
    }

    interface Outputs {
        fun finishActivity(): Observable<Unit>
        fun makeToast(): Observable<Pair<String, Int>>
    }

    class ViewModel(application: Application) : AndroidViewModel(application), Inputs, Outputs {
        private val repository: ArticleRepository by lazy { (application as BasicApp).getRepository() }

        private val article: PublishSubject<Article> = PublishSubject.create()

        private val finishActivity: BehaviorSubject<Unit> = BehaviorSubject.create()
        private val makeToast: BehaviorSubject<Pair<String, Int>> = BehaviorSubject.create()

        init {

        }

        override fun finishActivity(): Observable<Unit> = this.finishActivity

        override fun makeToast(): Observable<Pair<String, Int>> = this.makeToast

        override fun article(article: Article) {
            this.article.onNext(article)
        }
    }


}