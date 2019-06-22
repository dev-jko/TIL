package com.example.helloroom

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase

@Database(entities = [User::class], version = 1)
abstract class UserDatabase : RoomDatabase() {
    abstract fun UserDao(): UserDAO

    companion object {
        private var INSTANCE: UserDatabase? = null

        fun getInstance(context: Context): UserDatabase {
            if (INSTANCE == null) {
                synchronized(UserDatabase::class) {
                    INSTANCE =
                        Room.databaseBuilder(context.applicationContext, UserDatabase::class.java, "Sample.db")
                            .allowMainThreadQueries() // 테스트용으로 임시 허용한 것, 원래 db를 메인스레드에서 사용하면 안됨!!
                            .build()
                }
            }
            return INSTANCE as UserDatabase
        }

    }

}