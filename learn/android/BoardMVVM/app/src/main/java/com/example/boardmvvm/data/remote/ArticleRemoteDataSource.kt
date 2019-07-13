package com.example.boardmvvm.data.remote

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import com.example.boardmvvm.ArticleDataSource
import com.example.boardmvvm.data.Article

object ArticleRemoteDataSource : ArticleDataSource {
    override fun getAllArticles(): LiveData<List<Article>> {
        // TODO
        return MutableLiveData<List<Article>>()
    }

    override fun getArticle(articleId: Long): LiveData<Article> {
        // TODO
        return MutableLiveData<Article>()
    }

    override fun insertArticle(article: Article) {
        // TODO
    }
}