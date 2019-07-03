package com.example.boardmvc.controller

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.boardmvc.R
import com.example.boardmvc.model.ArticlesDatabase
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.rxkotlin.addTo
import io.reactivex.schedulers.Schedulers
import kotlinx.android.synthetic.main.activity_detail.*

class DetailActivity : AppCompatActivity() {

    private val db: ArticlesDatabase by lazy {
        ArticlesDatabase.getInstance(this)
    }
    private val compositeDisposable = CompositeDisposable()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_detail)

        val articleId = intent.extras!!.getLong("articleId")
        db.articleDao().getArticle(articleId)
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
