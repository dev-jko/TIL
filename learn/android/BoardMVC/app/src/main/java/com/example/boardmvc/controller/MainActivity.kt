package com.example.boardmvc.controller

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.boardmvc.R
import com.example.boardmvc.model.Article
import com.example.boardmvc.model.ArticlesDatabase
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.rxkotlin.addTo
import io.reactivex.schedulers.Schedulers
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    private val TAG = MainActivity::class.java.simpleName
    private val db: ArticlesDatabase by lazy {
        ArticlesDatabase.getInstance(this)
    }
    private val callback = object : MyClickCallback {
        override fun onClick(article: Article) {
            val intent = Intent(this@MainActivity, DetailActivity::class.java)
            intent.putExtra("articleId", article.articleId)
            startActivity(intent)
        }
    }
    private val adapter: ArticleAdapter = ArticleAdapter(this.callback)
    private val compositeDisposable = CompositeDisposable()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        rv_article.adapter = adapter

        db.articleDao().getAllArticles()
            .observeOn(Schedulers.io())
            .subscribeOn(AndroidSchedulers.mainThread())
            .subscribe { adapter.updateArticles(it) }
            .addTo(compositeDisposable)

    }

    override fun onDestroy() {
        super.onDestroy()
        compositeDisposable.dispose()
    }

}
