package com.myproject.myapplication

import android.content.Context
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteOpenHelper

class CalendarOpenHelper(
    context: Context,
    DATABASE_NAME: String = "myApp.sqlite3",
    DATABASE_VERSION: Int = 1
) : SQLiteOpenHelper(
    context, DATABASE_NAME,
    null, DATABASE_VERSION
) {

    override fun onCreate(db: SQLiteDatabase?) {
        val TABLE_NAME = "calendar"
        val createTable = "CREATE TABLE IF NOT EXISTS $TABLE_NAME (" +
                "ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT," +
                "START_DATE DATE," +
                "END_DATE DATE," +
                "CONTENT TEXT" +
                ");"
        db!!.execSQL(createTable)
    }

    override fun onUpgrade(db: SQLiteDatabase?, oldVersion: Int, newVersion: Int) {
        onCreate(db)
    }
}