package com.example.boardmvc.controller

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.boardmvc.R
import com.example.boardmvc.model.ArticlesDatabase
import kotlinx.android.synthetic.main.activity_detail.*

class DetailActivity : AppCompatActivity() {

    private val db: ArticlesDatabase by lazy {
        ArticlesDatabase.getInstance(this)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_detail)

        val articleId = intent.extras.getLong("articleId")

        db.


        detail_title_tv.text = ""
        detail_content_tv.text = ""
    }
}
