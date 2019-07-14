package com.example.boardmvvmrx.data

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.PrimaryKey


@Entity(tableName = "articles")
data class Article(
    @ColumnInfo(name = "title") val title: String,
    @ColumnInfo(name = "content") val content: String
) {
    @PrimaryKey(autoGenerate = true)
    var articleId: Long = 0
}