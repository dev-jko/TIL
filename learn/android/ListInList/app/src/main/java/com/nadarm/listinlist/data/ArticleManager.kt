package com.nadarm.listinlist.data

object ArticleManager {

    private val _articles: MutableList<Article> = ArrayList<Article>()
    val articles: List<Article> get() = _articles
    private var index: Long = 0

    init {
        listOf(
            Article("test1", "content"),
            Article("test2", "content"),
            Article("test3", "content"),
            Article("test4", "content"),
            Article("test5", "content")
        ).forEach { _articles.add(it) }
    }

    fun addArticle(article: Article) {
        article.id = index++
        _articles.add(article)
    }


    fun getArticle(id: Long): Article? {
        return _articles.find { it.id == id }
    }

    fun updateArticle(article: Article) {
        val i = _articles.indexOfFirst { it.id == article.id }
        if (i >= 0) {
            _articles[i] = article
        }

    }

}