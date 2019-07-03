package com.example.boardmvc.model

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase

@Database(entities = [Article::class], version = 1)
abstract class ArticlesDatabase : RoomDatabase() {

    abstract fun articleDao(): ArticleDao

    companion object {
        private var INSTANCE: ArticlesDatabase? = null

        fun getInstance(context: Context):ArticlesDatabase {
            return INSTANCE ?: synchronized(this) {
                INSTANCE ?: buildDatabase(context).also { INSTANCE = it }
            }
        }

        private fun buildDatabase(context: Context): ArticlesDatabase {
            return Room.databaseBuilder(
                context.applicationContext,
                ArticlesDatabase::class.java, "board.db"
            ).allowMainThreadQueries()
                .build()
        }

    }


}