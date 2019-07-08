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
import com.example.boardmvp.view.list.adapter.ArticleAdapterContract
import com.example.boardmvp.view.list.presenter.ListContract
import com.example.boardmvp.view.list.presenter.ListPresenter
import com.example.boardmvp.view.newArticle.NewArticleActivity
import kotlinx.android.synthetic.main.activity_main.*

class ListActivity : AppCompatActivity(), ListContract.View {

    private val TAG = ListActivity::class.java.simpleName
    private lateinit var presenter: ListContract.Presenter
    private val callback = object : MyClickCallback {
        override fun onClick(article: Article) {
            val intent = Intent(this@ListActivity, DetailActivity::class.java)
            intent.putExtra("articleId", article.articleId)
            startActivity(intent)
        }
    }
    private lateinit var adapterView: ArticleAdapterContract.View

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val adapter: ArticleAdapter = ArticleAdapter(callback)
        rv_article.adapter = adapter
        adapterView = adapter

        presenter = ListPresenter(this, adapter, (application as BasicApp).getRepository())

        floatingActionButton.setOnClickListener {
            presenter.onAddButtonClick()
        }

        presenter.onCreate()
    }

    override fun startNewArticleActivity() {
        val intent = Intent(this, NewArticleActivity::class.java)
        startActivity(intent)
    }

    override fun refresh() {
        adapterView.refresh()
    }

    override fun onDestroy() {
        super.onDestroy()
        presenter.onDestroy()
    }

}
