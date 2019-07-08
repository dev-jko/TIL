package com.example.boardmvp.view.list.presenter

interface ListContract {
    interface View{
        fun refresh()
        fun startNewArticleActivity()
    }

    interface Presenter{
        fun onCreate()
        fun onDestroy()
        fun onAddButtonClick()
    }
}