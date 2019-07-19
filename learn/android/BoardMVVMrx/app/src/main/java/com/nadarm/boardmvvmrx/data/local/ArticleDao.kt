package com.nadarm.boardmvvmrx.data.local

import androidx.room.*
import com.nadarm.boardmvvmrx.data.Article
import io.reactivex.Flowable
import io.reactivex.Observable
import io.reactivex.Single

@Dao
interface ArticleDao {
    @Query("SELECT * FROM articles ORDER BY articleId DESC")
    fun getAllArticles(): Flowable<List<Article>>

    @Query("SELECT * FROM articles WHERE articleId = :articleId")
    fun getArticle(articleId: Long): Observable<Article>

    @Insert(onConflict = OnConflictStrategy.ABORT)
    fun insertArticle(article: Article): Single<Long>

    @Update
    fun updateArticle(article: Article): Single<Int>

    @Delete
    fun deleteArticle(article: Article): Single<Int>
}
