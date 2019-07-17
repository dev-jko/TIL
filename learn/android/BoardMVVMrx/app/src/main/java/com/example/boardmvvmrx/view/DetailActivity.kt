package com.example.boardmvvmrx.view

import android.content.Intent
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import androidx.appcompat.app.AppCompatActivity
import androidx.databinding.DataBindingUtil
import androidx.lifecycle.ViewModelProviders
import com.example.boardmvvmrx.R
import com.example.boardmvvmrx.databinding.ActivityDetailBinding
import com.example.boardmvvmrx.viewModel.DetailViewModel
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.rxkotlin.addTo

class DetailActivity : AppCompatActivity() {

    private val compositeDisposable: CompositeDisposable = CompositeDisposable()
    private val binding: ActivityDetailBinding by lazy {
        DataBindingUtil.setContentView<ActivityDetailBinding>(this, R.layout.activity_detail)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val detailVm = ViewModelProviders.of(this).get(DetailViewModel.ViewModel::class.java)
        binding.detailVm = detailVm
        binding.lifecycleOwner = this

        detailVm.inputs.intent(intent)

        detailVm.outputs.article()
            .observeOn(AndroidSchedulers.mainThread())
            .subscribe { article ->
                binding.detailTitleTv.text = article.title
                binding.detailContentTv.text = article.content
            }
            .addTo(compositeDisposable)

        detailVm.outputs.startEditActivity()
            .observeOn(AndroidSchedulers.mainThread())
            .subscribe { startEditActivity(it) }
            .addTo(compositeDisposable)
    }

    private fun startEditActivity(articleId: Long) {
        val intent = Intent(this, EditActivity::class.java)
        println(articleId)
        intent.putExtra("articleId", articleId)
        startActivity(intent)
    }

    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        super.onCreateOptionsMenu(menu)
        menuInflater.inflate(R.menu.edit_actionbar_actions, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem?): Boolean {
        if (item!!.itemId == R.id.edit_actionbar) {
            binding.detailVm!!.inputs.editClicked()
        }
        return super.onOptionsItemSelected(item)
    }

    override fun onDestroy() {
        super.onDestroy()
        compositeDisposable.dispose()
    }
}