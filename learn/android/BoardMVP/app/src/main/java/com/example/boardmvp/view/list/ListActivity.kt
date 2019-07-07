package com.example.boardmvp.view.list

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.boardmvp.ArticleRepository
import com.example.boardmvp.R
import com.example.boardmvp.view.list.adapter.ArticleAdapter
import com.example.boardmvp.view.detail.DetailActivity
import com.example.boardmvp.MyClickCallback
import com.example.boardmvp.view.newArticle.NewArticleActivity
import com.example.boardmvp.data.Article
import com.example.boardmvp.data.local.ArticleDatabase
import com.example.boardmvp.data.local.ArticleLocalDataSource
import com.example.boardmvp.data.remote.ArticleRemoteDataSource
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.rxkotlin.addTo
import io.reactivex.schedulers.Schedulers
import kotlinx.android.synthetic.main.activity_main.*

class ListActivity : AppCompatActivity() {

    private val TAG = ListActivity::class.java.simpleName
    private val repository: ArticleRepository by lazy {
        ArticleRepository.getInstance(
            ArticleLocalDataSource.getInstance(ArticleDatabase.getInstance(application).articleDao()),
            ArticleRemoteDataSource
            )
    }
    private val callback = object : MyClickCallback {
        override fun onClick(article: Article) {
            val intent = Intent(this@ListActivity, DetailActivity::class.java)
            intent.putExtra("articleId", article.articleId)
            startActivity(intent)
        }
    }
    private val adapter: ArticleAdapter =
        ArticleAdapter(this.callback)
    private val compositeDisposable = CompositeDisposable()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        rv_article.adapter = adapter
        repository.getAllArticles()
            .subscribeOn(Schedulers.io())
            .observeOn(AndroidSchedulers.mainThread())
            .subscribe { adapter.updateArticles(it) }
            .addTo(compositeDisposable)

        floatingActionButton.setOnClickListener {
            val intent = Intent(this, NewArticleActivity::class.java)
            startActivity(intent)
        }

    }

    override fun onDestroy() {
        super.onDestroy()
        compositeDisposable.dispose()
    }

}
