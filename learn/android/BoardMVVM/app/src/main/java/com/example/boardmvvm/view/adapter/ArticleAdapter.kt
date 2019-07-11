package com.example.boardmvvm.view.adapter

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.databinding.DataBindingUtil
import androidx.recyclerview.widget.RecyclerView
import com.example.boardmvvm.MyClickCallback
import com.example.boardmvvm.R
import com.example.boardmvvm.data.Article
import com.example.boardmvvm.databinding.ArticleItemBinding

class ArticleAdapter(private val callback: MyClickCallback) : RecyclerView.Adapter<ArticleAdapter.ViewHolder>() {

    private var articles: List<Article> = emptyList()

    fun refresh(newArticles: List<Article>) {
        articles = newArticles
        notifyDataSetChanged()
    }

    override fun getItemCount(): Int {
        return articles.size
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val inflater = LayoutInflater.from(parent.context)
        val binding = DataBindingUtil.inflate<ArticleItemBinding>(inflater, R.layout.article_item, parent, false)
        return ViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(articles[position], callback)
    }


    class ViewHolder(private val binding: ArticleItemBinding) : RecyclerView.ViewHolder(binding.root) {
        fun bind(article: Article, callback: MyClickCallback) {
            binding.article = article
            binding.callback = callback
        }
    }


}