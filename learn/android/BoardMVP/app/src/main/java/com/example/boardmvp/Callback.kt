package com.example.boardmvp

import com.example.boardmvp.data.Article

interface MyClickCallback {
    fun onClick(article: Article)
}