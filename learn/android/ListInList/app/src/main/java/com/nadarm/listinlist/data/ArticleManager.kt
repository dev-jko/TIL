package com.nadarm.listinlist.data

object ArticleManager {

    private val _articles: MutableList<Article> = ArrayList<Article>()
    val articles: List<Article> get() = _articles
    private var index: Long = 0

    init {
        listOf(
            Article(1, "test1", "content"),
            Article(2, "test2", "content"),
            Article(3, "test3", "content"),
            Article(4, "test4", "content"),
            Article(5, "test5", "content")
        ).forEach { _articles.add(it) }
    }

    fun addArticle(article: Article) {
        article.id = index++
        _articles.add(article)
    }

    fun getArticle(id: Long): Article? {
        return _articles.find { it.id == id }
    }

}