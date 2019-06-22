package com.example.helloroom

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "users")
data class User(
    val firstName: String,
    val lastName: String,
    val age: Int
){
    @PrimaryKey(autoGenerate = true) var id: Long = 0
}