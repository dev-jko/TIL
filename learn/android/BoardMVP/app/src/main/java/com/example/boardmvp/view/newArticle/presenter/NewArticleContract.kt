package com.example.boardmvp.view.newArticle.presenter

interface NewArticleContract {

    interface View {
        fun getTitleText(): String
        fun getContentText(): String
        fun makeToast(message: String)
        fun finish()
    }

    interface Presenter {
        fun onDestroy()
        fun onSaveButtonClicked()
    }
}