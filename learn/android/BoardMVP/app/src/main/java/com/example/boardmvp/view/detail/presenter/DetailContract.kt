package com.example.boardmvp.view.detail.presenter

interface DetailContract {
    interface View {
        fun getArticleIdFromIntent():Long
        fun showArticle(title:String, content:String)
    }

    interface Presenter {
        fun onCreate()
        fun onDestroy()
    }
}