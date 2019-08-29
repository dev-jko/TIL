package com.nadarm.listinlist.ui

import com.nadarm.listinlist.data.Article

sealed class MainItem {
    abstract fun getType(): ItemType
    abstract fun getItem(): Any

    class ArticlesItem(private val item: List<Article>) : MainItem() {
        override fun getType(): ItemType = ItemType.ARTICLES
        override fun getItem(): List<Article> = item
    }

    class ArticleItem(private val item: Article) : MainItem() {
        override fun getType(): ItemType = ItemType.ARTICLE
        override fun getItem(): Article = item
    }
}

enum class ItemType {
    ARTICLE,
    ARTICLES
}
