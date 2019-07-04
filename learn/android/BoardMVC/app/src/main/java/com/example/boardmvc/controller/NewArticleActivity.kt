package com.example.boardmvc.controller

import android.os.Bundle
import android.util.Log
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.boardmvc.ArticleRepository
import com.example.boardmvc.R
import com.example.boardmvc.model.Article
import io.reactivex.Observable
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.rxkotlin.addTo
import io.reactivex.schedulers.Schedulers
import kotlinx.android.synthetic.main.activity_new_article.*
import java.util.concurrent.TimeUnit

class NewArticleActivity : AppCompatActivity() {

    private val TAG = NewArticleActivity::class.java.simpleName
    private val repository: ArticleRepository by lazy { ArticleRepository(application) }
    private val compositeDisposable = CompositeDisposable()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_new_article)
    }

    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        super.onCreateOptionsMenu(menu)
        menuInflater.inflate(R.menu.actionbar_actions, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem?): Boolean {
        if (item!!.itemId == R.id.save_actionbar) {
            val newArticle = getNewArticle()
            insertArticle(newArticle)
        }
        return super.onOptionsItemSelected(item)
    }

    private fun getNewArticle(): Article {
        return Article(
            new_title_et.text.toString(),
            new_content_et.text.toString()
        )
    }

    private fun insertArticle(article: Article) {
        repository.insertArticle(article)
            .subscribeOn(Schedulers.io())
            .observeOn(AndroidSchedulers.mainThread())
            .subscribe(
                {
                    Log.i(TAG, "insertion completed")
                    onInsertionCompleted()
                },
                { it.printStackTrace() }
            ).addTo(compositeDisposable)
    }

    private fun onInsertionCompleted() {
        Toast.makeText(this, "글이 작성됐습니다.", Toast.LENGTH_SHORT).show()
        Observable.just(1)
            .subscribeOn(Schedulers.computation())
            .delay(1, TimeUnit.SECONDS)
            .observeOn(AndroidSchedulers.mainThread())
            .subscribe { finish() }
            .addTo(compositeDisposable)
    }


}
