package com.example.boardmvvm.view

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.databinding.DataBindingUtil
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProviders
import com.example.boardmvvm.R
import com.example.boardmvvm.data.Article
import com.example.boardmvvm.databinding.ActivityMainBinding
import com.example.boardmvvm.view.adapter.ArticleAdapter
import com.example.boardmvvm.viewModel.ListViewModel

class ListActivity : AppCompatActivity() {

    private val TAG = ListActivity::class.java.simpleName
    private val binding: ActivityMainBinding by lazy {
        DataBindingUtil.setContentView<ActivityMainBinding>(this, R.layout.activity_main)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val vm = ViewModelProviders.of(this).get(ListViewModel.ViewModel::class.java)
        binding.vm = vm
        binding.lifecycleOwner = this

        val adapter: ArticleAdapter = ArticleAdapter(vm)
        binding.rvArticle.adapter = adapter

        vm.outputs.articles().observe(this, Observer { articles -> adapter.refresh(articles) })
        vm.outputs.startDetailActivity().observe(this, Observer { article -> startDetailActivity(article) })
        vm.outputs.startNewArticleActivity().observe(this, Observer { isStart -> if (isStart) startNewArticleActivity() })
    }

    private fun startDetailActivity(article: Article) {
        val intent = Intent(this@ListActivity, DetailActivity::class.java)
        intent.putExtra("articleId", article.articleId)
        startActivity(intent)
    }

    private fun startNewArticleActivity() {
        val intent = Intent(this, NewArticleActivity::class.java)
        startActivity(intent)
    }

}
