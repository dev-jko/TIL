package com.nadarm.listinlist.data

import android.app.Application
import androidx.room.Room
import dagger.Module
import dagger.Provides
import javax.inject.Singleton


@Module
object DataProvideModule {

    @Singleton
    @JvmStatic
    @Provides
    fun provideDao(application: Application): ArticleDao {
        return Room.databaseBuilder(application, ArticleDatabase::class.java, "db")
            .build()
            .articleDao()
    }

}