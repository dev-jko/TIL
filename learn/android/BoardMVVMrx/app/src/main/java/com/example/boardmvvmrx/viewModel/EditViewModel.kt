package com.example.boardmvvmrx.viewModel

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import com.example.boardmvvmrx.ArticleRepository
import com.example.boardmvvmrx.BasicApp
import io.reactivex.disposables.CompositeDisposable

interface EditViewModel {

    interface Inputs {

    }

    interface Outputs {

    }

    class ViewModel(application: Application) : AndroidViewModel(application), Inputs, Outputs {
        private val compositeDisposable: CompositeDisposable = CompositeDisposable()
        private val repository: ArticleRepository by lazy { (application as BasicApp).getRepository() }


        override fun onCleared() {
            super.onCleared()
            compositeDisposable.dispose()
        }

    }

}