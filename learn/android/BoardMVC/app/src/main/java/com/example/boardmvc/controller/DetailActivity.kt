package com.example.boardmvc.controller

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.boardmvc.ArticleRepository
import com.example.boardmvc.R
import com.example.boardmvc.model.local.ArticleDatabase
import com.example.boardmvc.model.local.ArticleLocalDataSource
import com.example.boardmvc.model.remote.ArticleRemoteDataSource
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.rxkotlin.addTo
import io.reactivex.schedulers.Schedulers
import kotlinx.android.synthetic.main.activity_detail.*

class DetailActivity : AppCompatActivity() {

    private val repository: ArticleRepository by lazy {
        ArticleRepository.getInstance(
            ArticleLocalDataSource.getInstance(ArticleDatabase.getInstance(application).articleDao()),
            ArticleRemoteDataSource
        )
    }
    private val compositeDisposable = CompositeDisposable()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_detail)

        val articleId = intent.extras!!.getLong("articleId")
        repository.getArticle(articleId)
            .subscribeOn(Schedulers.io())
            .observeOn(AndroidSchedulers.mainThread())
            .subscribe(
                {
                    detail_title_tv.text = it.title
                    detail_content_tv.text = it.content
                },
                { it.printStackTrace() }
            ).addTo(compositeDisposable)
    }

    override fun onDestroy() {
        super.onDestroy()
        compositeDisposable.dispose()
    }

}
