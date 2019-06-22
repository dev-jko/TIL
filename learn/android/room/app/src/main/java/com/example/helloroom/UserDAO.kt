package com.example.helloroom

import androidx.room.*

@Dao
interface UserDAO {

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    fun insertUsers(vararg users: User)

    @Delete
    fun deleteUsers(vararg users: User)

    @Query("SELECT * FROM users")
    fun loadAllUsers(): List<User>

    @Query("SELECT * FROM users WHERE age BETWEEN :minAge AND :maxAge")
    fun loadAllUsersBetweenAges(minAge: Int, maxAge: Int): Array<User>

    @Query("SELECT * FROM users WHERE firstName IN (:firstNames)")
    fun loadAllUsersFromFirstNames(firstNames: List<String>): List<User>

}