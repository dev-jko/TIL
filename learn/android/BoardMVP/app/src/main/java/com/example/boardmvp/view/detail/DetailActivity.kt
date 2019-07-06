package com.example.boardmvp.view.detail

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.boardmvp.ArticleRepository
import com.example.boardmvp.R
import com.example.boardmvp.data.local.ArticleDatabase
import com.example.boardmvp.data.local.ArticleLocalDataSource
import com.example.boardmvp.data.remote.ArticleRemoteDataSource
import com.example.boardmvp.view.detail.presenter.DetailContract
import com.example.boardmvp.view.detail.presenter.DetailPresenter
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.rxkotlin.addTo
import io.reactivex.schedulers.Schedulers
import kotlinx.android.synthetic.main.activity_detail.*

class DetailActivity : AppCompatActivity(), DetailContract.View {

    private val presenter: DetailContract.Presenter = DetailPresenter(this)

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_detail)

        presenter.onCreate()
    }

    override fun onDestroy() {
        super.onDestroy()
        presenter.onDestroy()
    }

    override fun getArticleIdFromIntent():Long {
        return intent.extras!!.getLong("articleId")
    }

    override fun showArticle(title: String, content: String) {
        detail_title_tv.text = title
        detail_content_tv.text = content
    }
}
