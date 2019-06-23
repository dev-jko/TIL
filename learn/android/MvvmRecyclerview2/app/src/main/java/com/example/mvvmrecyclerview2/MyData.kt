package com.example.mvvmrecyclerview2

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "myData")
data class MyData(
    val name: String,
    val age: Int
) {
    @PrimaryKey(autoGenerate = true)
    var id: Long = 0
}
