package com.example.boardmvvm.view.adapter

import com.example.boardmvvm.data.Article

interface ArticleAdapterContract {
    interface View {
        fun refresh()
    }

    interface Model {
        fun getItemCount(): Int
        fun changeList(list: List<Article>)
    }
}