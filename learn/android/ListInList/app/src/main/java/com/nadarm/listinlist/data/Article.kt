package com.nadarm.listinlist.data

data class Article(
    var id: Long? = null,
    val title: String,
    val content: String
) {
    var views: Int = 0
        private set

    fun view() {
        views++
    }
}