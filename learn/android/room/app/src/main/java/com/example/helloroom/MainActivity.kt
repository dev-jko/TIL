package com.example.helloroom

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.room.Room
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

//        val db = Room.databaseBuilder(applicationContext, UserDatabase::class.java, "Sample.db")
//            .allowMainThreadQueries() // 테스트용으로 임시 허용한 것, 원래 db를 메인스레드에서 사용하면 안됨!!
//            .build()
        val db = UserDatabase.getInstance(this)
        // 테스트용으로 임시 허용한 것, 원래 db를 메인스레드에서 사용하면 안됨!!


        db.UserDao().insertUsers(
            User("first", "last", 20),
            User("test1", "test2", 21)
        )

        val users = db.UserDao().loadAllUsers()
        tv.text = users.toString()
    }
}
