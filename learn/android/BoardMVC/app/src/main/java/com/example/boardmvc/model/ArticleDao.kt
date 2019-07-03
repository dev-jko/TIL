package com.example.boardmvc.model

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import io.reactivex.Completable
import io.reactivex.Flowable

@Dao
interface ArticleDao {
    @Query("SELECT * FROM articles")
    fun getAllArticles(): Flowable<List<Article>>

    @Query("SELECT * FROM articles WHERE articleId = :articleId")

    @Insert(onConflict = OnConflictStrategy.ABORT)
    fun insertArticle(article: Article): Completable
}
