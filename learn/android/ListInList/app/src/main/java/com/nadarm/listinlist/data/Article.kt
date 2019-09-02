package com.nadarm.listinlist.data

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity
data class Article(
    val title: String,
    val content: String
) {
    @PrimaryKey(autoGenerate = true)
    var id: Long = 0
    var views: Int = 0
}