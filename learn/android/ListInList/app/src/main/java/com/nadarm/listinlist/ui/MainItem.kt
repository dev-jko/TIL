package com.nadarm.listinlist.ui

import com.nadarm.listinlist.data.Article

sealed class MainItem {
    abstract fun getType(): ItemType
    abstract fun getItem(): Any

    class HeaderItem(private val item: String) : MainItem() {
        override fun getType(): ItemType = ItemType.HEADER
        override fun getItem(): String = item
    }

    class ArticlesItem(private val item: List<MainItem>) : MainItem() {
        override fun getType(): ItemType = ItemType.ARTICLES
        override fun getItem(): List<MainItem> = item
    }

    class ArticleItem(private val item: Article) : MainItem() {
        override fun getType(): ItemType = ItemType.ARTICLE
        override fun getItem(): Article = item
    }

    class ArticlePreviewItem(private val item: Article) : MainItem() {
        override fun getType(): ItemType = ItemType.PREVIEW
        override fun getItem(): Article = item
    }
}

enum class ItemType {
    PREVIEW,
    HEADER,
    ARTICLE,
    ARTICLES
}
