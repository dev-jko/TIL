package com.example.boardmvvm.view

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.databinding.DataBindingUtil
import androidx.lifecycle.ViewModelProviders
import com.example.boardmvvm.R
import com.example.boardmvvm.databinding.ActivityDetailBinding
import com.example.boardmvvm.viewModel.DetailViewModel

class DetailActivity : AppCompatActivity() {

    private val binding: ActivityDetailBinding by lazy {
        DataBindingUtil.setContentView<ActivityDetailBinding>(this, R.layout.activity_detail)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding.vm = ViewModelProviders.of(this).get(DetailViewModel.ViewModel::class.java)
        binding.lifecycleOwner = this

        binding.vm!!.inputs.intent(intent)
    }

}