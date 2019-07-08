package com.example.boardmvp.view.list.adapter

import com.example.boardmvp.data.Article

interface ArticleAdapterContract {
    interface View {
        fun refresh()
    }

    interface Model {
        fun getItemCount(): Int
        fun changeList(list: List<Article>)
    }
}