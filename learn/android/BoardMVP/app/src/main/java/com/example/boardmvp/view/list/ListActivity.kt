package com.example.boardmvp.view.list

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.boardmvp.BasicApp
import com.example.boardmvp.MyClickCallback
import com.example.boardmvp.R
import com.example.boardmvp.data.Article
import com.example.boardmvp.view.detail.DetailActivity
import com.example.boardmvp.view.list.adapter.ArticleAdapter
import com.example.boardmvp.view.list.presenter.ListContract
import com.example.boardmvp.view.list.presenter.ListPresenter
import com.example.boardmvp.view.newArticle.NewArticleActivity
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.schedulers.Schedulers
import kotlinx.android.synthetic.main.activity_main.*

class ListActivity : AppCompatActivity(), ListContract.View {

    private val TAG = ListActivity::class.java.simpleName
    private val presenter: ListContract.Presenter by lazy {
        ListPresenter(this, (application as BasicApp).getRepository())
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
        presenter.onDestroy()
    }

}
