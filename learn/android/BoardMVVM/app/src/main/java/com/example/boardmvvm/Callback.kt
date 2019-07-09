package com.example.boardmvvm

import com.example.boardmvvm.data.Article

interface MyClickCallback {
    fun onClick(article: Article)
}