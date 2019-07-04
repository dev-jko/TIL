package com.example.boardmvc.controller

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.boardmvc.R
import com.example.boardmvc.model.Article

class ArticleAdapter(private val callback: MyClickCallback) : RecyclerView.Adapter<ArticleAdapter.ViewHolder>() {

    private var articles: List<Article> = emptyList()

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val inflater = parent.context.getSystemService(Context.LAYOUT_INFLATER_SERVICE) as LayoutInflater
        val view = inflater.inflate(R.layout.article_item, parent, false)
        return ViewHolder(view)
    }

    override fun getItemCount(): Int {
        return articles.size
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(articles[position], callback)
    }

    fun updateArticles(articles: List<Article>) {
        this.articles = articles
        notifyDataSetChanged()
    }


    class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {

        private val title: TextView = itemView.findViewById(R.id.title_tv)

        fun bind(article: Article, callback: MyClickCallback) {
            title.text = article.title
            itemView.setOnClickListener {
                callback.onClick(article)
            }
        }
    }


}