package com.example.boardmvvm.view

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.databinding.DataBindingUtil
import androidx.lifecycle.ViewModelProviders
import com.example.boardmvvm.BasicApp
import com.example.boardmvvm.MyClickCallback
import com.example.boardmvvm.R
import com.example.boardmvvm.data.Article
import com.example.boardmvvm.databinding.ActivityMainBinding
import com.example.boardmvvm.view.adapter.ArticleAdapter
import com.example.boardmvvm.view.adapter.ArticleAdapterContract
import com.example.boardmvvm.viewModel.ListViewModel
import kotlinx.android.synthetic.main.activity_main.*

class ListActivity : AppCompatActivity(){

    private val TAG = ListActivity::class.java.simpleName
    private val binding: ActivityMainBinding by lazy {
        DataBindingUtil.setContentView(this, R.layout.activity_main)
    }
    private val callback = object : MyClickCallback {
        override fun onClick(article: Article) {
            val intent = Intent(this@ListActivity, DetailActivity::class.java)
            intent.putExtra("articleId", article.articleId)
            startActivity(intent)
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding.vm = ViewModelProviders.of(this).get(ListViewModel::class.java)
        binding.lifecycleOwner = this

        val adapter: ArticleAdapter =
            ArticleAdapter(callback)
        rv_article.adapter = adapter
        adapterView = adapter

        floatingActionButton.setOnClickListener {
            presenter.onAddButtonClick()
        }

        presenter.onCreate()
    }

    override fun startNewArticleActivity() {
        val intent = Intent(this, NewArticleActivity::class.java)
        startActivity(intent)
    }

}
