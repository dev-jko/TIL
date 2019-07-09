package com.example.boardmvvm.view

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.boardmvvm.BasicApp
import com.example.boardmvvm.R
import com.example.boardmvvm.viewModel.DetailPresenter
import kotlinx.android.synthetic.main.activity_detail.*

class DetailActivity : AppCompatActivity(){

    private val presenter: DetailContract.Presenter by lazy {
        DetailPresenter(this, (application as BasicApp).getRepository())
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_detail)

        presenter.onCreate()
    }

    override fun onDestroy() {
        super.onDestroy()
        presenter.onDestroy()
    }

    fun getArticleIdFromIntent(): Long {
        return intent.extras!!.getLong("articleId")
    }

    fun showArticle(title: String, content: String) {
        detail_title_tv.text = title
        detail_content_tv.text = content
    }
}