package com.example.boardmvvmrx.data.local

import androidx.room.*
import com.example.boardmvvmrx.data.Article
import io.reactivex.Completable
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
}
