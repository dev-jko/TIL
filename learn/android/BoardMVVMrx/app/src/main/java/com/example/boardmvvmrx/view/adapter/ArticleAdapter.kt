package com.example.boardmvvmrx.view.adapter

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.databinding.DataBindingUtil
import androidx.recyclerview.widget.RecyclerView
import com.example.boardmvvmrx.R
import com.example.boardmvvmrx.data.Article
import com.example.boardmvvmrx.databinding.ArticleItemBinding

class ArticleAdapter(private val delegate: Delegate) : RecyclerView.Adapter<ArticleAdapter.ViewHolder>() {

    interface Delegate : ArticleAdapter.ViewHolder.Delegate

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
        holder.bind(articles[position], delegate)
    }


    class ViewHolder(private val binding: ArticleItemBinding) : RecyclerView.ViewHolder(binding.root) {

        interface Delegate {
            fun articleClicked(article: Article)
        }

        fun bind(article: Article, delegate: Delegate) {
            binding.titleTv.text = article.title
            binding.root.setOnClickListener { delegate.articleClicked(article) }
        }
    }


}