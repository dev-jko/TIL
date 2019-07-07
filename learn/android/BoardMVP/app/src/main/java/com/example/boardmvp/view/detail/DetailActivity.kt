package com.example.boardmvp.view.detail

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.boardmvp.BasicApp
import com.example.boardmvp.R
import com.example.boardmvp.view.detail.presenter.DetailContract
import com.example.boardmvp.view.detail.presenter.DetailPresenter
import kotlinx.android.synthetic.main.activity_detail.*

class DetailActivity : AppCompatActivity(), DetailContract.View {

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

    override fun getArticleIdFromIntent(): Long {
        return intent.extras!!.getLong("articleId")
    }

    override fun showArticle(title: String, content: String) {
        detail_title_tv.text = title
        detail_content_tv.text = content
    }
}