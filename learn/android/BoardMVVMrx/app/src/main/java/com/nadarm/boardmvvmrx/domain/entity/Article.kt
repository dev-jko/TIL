package com.nadarm.boardmvvmrx.domain.entity

data class Article(
    val articleId: Long,
    val title: String,
    val content: String
) {
    constructor(title: String, content: String) : this(0, title, content)
}