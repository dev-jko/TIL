package com.example.mvvmrecyclerview2

import androidx.lifecycle.LiveData
import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query

@Dao
interface MyDataDAO {

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    fun insertMyData(vararg myData: MyData)

    @Query("SELECT * FROM myData")
    fun loadAllMyData(): LiveData<List<MyData>>
}