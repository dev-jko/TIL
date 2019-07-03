package com.example.boardmvc.controller

import com.example.boardmvc.model.Article

interface MyClickCallback {
    fun onClick(article: Article)
}