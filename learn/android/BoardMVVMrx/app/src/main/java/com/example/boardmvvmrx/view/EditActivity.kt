package com.example.boardmvvmrx.view

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.databinding.DataBindingUtil
import androidx.lifecycle.ViewModelProviders
import com.example.boardmvvmrx.R
import com.example.boardmvvmrx.databinding.ActivityEditBinding
import com.example.boardmvvmrx.viewModel.EditViewModel
import io.reactivex.disposables.CompositeDisposable

class EditActivity : AppCompatActivity() {

    private val compositeDisposable: CompositeDisposable = CompositeDisposable()
    private val binding: ActivityEditBinding by lazy { DataBindingUtil.setContentView(this, R.layout.activity_edit) }


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val vm = ViewModelProviders.of(this).get(EditViewModel.ViewModel::class.java)
        binding.vm = vm
        binding.lifecycleOwner = this


    }

    override fun onDestroy() {
        super.onDestroy()
        compositeDisposable.dispose()
    }
}
