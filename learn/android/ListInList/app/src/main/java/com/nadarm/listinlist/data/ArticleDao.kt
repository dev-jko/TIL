package com.nadarm.listinlist.data

import androidx.room.Dao
import androidx.room.OnConflictStrategy
import androidx.room.Query
import androidx.room.Update
import io.reactivex.Completable
import io.reactivex.Single

@Dao
abstract class ArticleDao {

    @Query("SELECT * FROM article WHERE id == :id")
    abstract fun getArticle(id: Long): Single<Article>

    @Update(entity = Article::class, onConflict = OnConflictStrategy.REPLACE)
    abstract fun updateArticle(article: Article): Completable

}