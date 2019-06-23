package com.example.mvvmrecyclerview2

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase

@Database(entities = [MyData::class], version = 1)
abstract class MyDataDatabase : RoomDatabase() {
    abstract fun MyDataDao(): MyDataDAO

    companion object {
        private var INSTANCE: MyDataDatabase? = null

        fun getInstance(context: Context): MyDataDatabase {
            if (INSTANCE == null) {
                synchronized(MyDataDatabase::class) {
                    INSTANCE = Room.databaseBuilder(context.applicationContext, MyDataDatabase::class.java, "Sample.db")
                        .allowMainThreadQueries()  // 테스트용으로 임시 허용한 것, 원래 db를 메인스레드에서 사용하면 안됨!!
                        .build()
                }
            }
            return INSTANCE as MyDataDatabase
        }

    }
}