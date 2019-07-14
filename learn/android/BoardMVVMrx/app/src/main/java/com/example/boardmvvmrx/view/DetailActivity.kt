package com.example.boardmvvmrx.view

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.databinding.DataBindingUtil
import androidx.lifecycle.ViewModelProviders
import com.example.boardmvvmrx.R
import com.example.boardmvvmrx.databinding.ActivityDetailBinding
import com.example.boardmvvmrx.viewModel.DetailViewModel
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.rxkotlin.addTo
import io.reactivex.schedulers.Schedulers

class DetailActivity : AppCompatActivity() {

    private val compositeDisposable: CompositeDisposable = CompositeDisposable()
    private val binding: ActivityDetailBinding by lazy {
        DataBindingUtil.setContentView<ActivityDetailBinding>(this, R.layout.activity_detail)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val vm = ViewModelProviders.of(this).get(DetailViewModel.ViewModel::class.java)
        binding.vm = vm
        binding.lifecycleOwner = this

        vm.inputs.intent(intent)
        vm.outputs.article()
            .observeOn(AndroidSchedulers.mainThread())
            .subscribe { article ->
                binding.detailTitleTv.text = article.title
                binding.detailContentTv.text = article.content
            }
            .addTo(compositeDisposable)
    }

    override fun onDestroy() {
        super.onDestroy()
        compositeDisposable.dispose()
    }
}