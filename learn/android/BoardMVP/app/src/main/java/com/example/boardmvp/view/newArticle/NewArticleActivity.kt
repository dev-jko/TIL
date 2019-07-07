package com.example.boardmvp.view.newArticle

import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.boardmvp.BasicApp
import com.example.boardmvp.R
import com.example.boardmvp.view.newArticle.presenter.NewArticleContract
import com.example.boardmvp.view.newArticle.presenter.NewArticlePresenter
import kotlinx.android.synthetic.main.activity_new_article.*

class NewArticleActivity : AppCompatActivity(), NewArticleContract.View {

    private val TAG = NewArticleActivity::class.java.simpleName
    private val presenter: NewArticleContract.Presenter by lazy {
        NewArticlePresenter(this, (application as BasicApp).getRepository())
    }

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
            presenter.onSaveButtonClicked()
        }
        return super.onOptionsItemSelected(item)
    }

    override fun onDestroy() {
        super.onDestroy()
        presenter.onDestroy()
    }

    override fun getTitleText(): String {
        return new_title_et.text.toString()
    }

    override fun getContentText(): String {
        return new_content_et.text.toString()
    }

    override fun makeToast(message: String) {
        Toast.makeText(this, message, Toast.LENGTH_SHORT).show()
    }

}
