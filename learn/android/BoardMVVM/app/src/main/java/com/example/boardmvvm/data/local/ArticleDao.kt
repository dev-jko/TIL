package com.example.boardmvvm.data.local

import androidx.lifecycle.LiveData
import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import com.example.boardmvvm.data.Article
import io.reactivex.Completable
import io.reactivex.Flowable
import io.reactivex.Single
import java.util.concurrent.Callable

@Dao
interface ArticleDao {
    @Query("SELECT * FROM articles ORDER BY articleId DESC")
    fun getAllArticles(): LiveData<List<Article>>

    @Query("SELECT * FROM articles WHERE articleId = :articleId")
    fun getArticle(articleId: Long): LiveData<Article>

    @Insert(onConflict = OnConflictStrategy.ABORT)
    fun insertArticle(article: Article)
}
